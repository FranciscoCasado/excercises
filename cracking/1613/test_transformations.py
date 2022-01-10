import unittest

from geometry_elements import Point, Segment, Square, Line
from transformations import Bisector

class TestBisector(unittest.TestCase):
    def test_bisect_squares(self):
        s1 = Square(Point(0,0), 10)
        s2 = Square(Point(0,5), 10)
        b = Bisector()
        l = b.bisect_squares(s1, s2)
        self.assertEqual(l, Line(Point(5,5), Point(5,10)))
        self.assertEqual(l.start, Point(5,5))
        self.assertEqual(l.end,  Point(5,10))


if __name__ == "__main__":
    unittest.main()
