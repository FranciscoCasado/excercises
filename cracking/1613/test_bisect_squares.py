import unittest

from bisect_squares import Square, Line, Point, Bisector

class TestPoint(unittest.TestCase):
    def test_create_point(self):
        p = Point(38,44)
        self.assertEqual(p, (38,44))
        self.assertEqual(p.x, 38)
        self.assertEqual(p.y, 44)
    
    def test_add_two_points(self):
        p = Point(10,5)
        q = Point(4,6)
        self.assertEqual(p+q, (14,11))

class TestSquares(unittest.TestCase):
    def test_create_squares(self):
        s = Square(Point(0, 0), 10)
        self.assertEqual(s.center, (5, 5))

        s = Square(Point(10, 10), -20)
        self.assertEqual(s.center, (0, 0))

class TestSquares(unittest.TestCase):
    def test_create_line(self):
        l = Line(Point(0, 0), Point(1, 1))
        self.assertEqual(l._m, 1)
        self.assertEqual(l._n, 0)

class TestBisector(unittest.TestCase):
    def test_bisect_squares(self):
        s1 =Square(Point(0,0), 10)
        s2 =Square(Point(0,5), 10)
        b = Bisector()
        l = b.bisect_squares(s1, s2)
        self.assertEqual(l, Line(Point(5,5), Point(15,15)))


if __name__ == "__main__":
    unittest.main()
