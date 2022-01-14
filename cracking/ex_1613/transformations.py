from .geometry_elements import Square, Line, Segment, Point


class Bisector:
    def bisect_squares(self, first: Square, second: Square) -> Point:
        return Line(first.center, second.center)
