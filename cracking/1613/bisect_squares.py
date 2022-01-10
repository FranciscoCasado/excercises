

class Point(tuple):
    def __new__(cls, x, y):
        return super(Point, cls).__new__(cls, (float(x),float(y)))
    
    @property
    def x(self):
        return self[0]
    
    @property
    def y(self):
        return self[1]

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(f"'{other}' is of type {other.__class__}, it cannot be added to a Point")

        return Point(self.x + other.x, self.y + other.y)

class Square:
    def __init__(self, origin: Point, side):
        self.origin = origin
        self._a = side

    @property
    def center(self):
        return Point(self.origin.x + self._a/2, self.origin.y + self._a/2)

class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
        
        if start.x == end.x:
            self._m = float("Inf")
        else:
            self._m = (end.y - start.y) / (end.x - start.x)
        self._n = start.y - start.x * self._m

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(f"'{other}' is of type {other.__class__}, it cannot be compared to a Line")

        return (self._m == other._m) and (self._n == other._n)

    

class Bisector:
    def bisect_squares(self, first: Square, second: Square) -> Point:
        return Line(first.center, second.center)