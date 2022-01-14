import unittest

from cracking.ex_1613.geometry_elements import Square, Line, Point, Segment

class TestPoint(unittest.TestCase):
    def test_create_point(self):
        p = Point(38, 44)
        self.assertEqual(p, (38, 44))
        self.assertEqual(p.x, 38)
        self.assertEqual(p.y, 44)

    def test_add_two_points(self):
        p = Point(10, 5)
        q = Point(4, 6)
        self.assertEqual(p + q, (14, 11))

    def test_dot_product_two_points(self):
        p = Point(10, 5)
        q = Point(4, 6)
        r = Point(-1, 0)
        self.assertEqual(p * q, 70)
        self.assertEqual(p * r, -10)


class TestSquare(unittest.TestCase):
    def test_create_squares(self):
        s = Square(Point(0, 0), 10)
        self.assertEqual(s.center, (5, 5))

        s = Square(Point(10, 10), -20)
        self.assertEqual(s.center, (0, 0))


class TestLine(unittest.TestCase):
    def test_create_line(self):
        l = Line(Point(0, 0), Point(1, 1))
        self.assertEqual(l._m, 1)
        self.assertEqual(l._n, 0)


class TestSegment(unittest.TestCase):
    def test_create_segment(self):
        s1 = Segment(Point(0, 0), Point(1, 1))
        s2 = Segment(Point(1, 1), Point(0, 0))
        self.assertEqual(s1, s2)
        self.assertEqual(s2, s1)


if __name__ == "__main__":
    unittest.main()
