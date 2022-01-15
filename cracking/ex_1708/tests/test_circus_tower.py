import unittest

from cracking.ex_1708.circus_tower import largest_tower


class TestCircusTower(unittest.TestCase):
    def test_one_person_tower(self):
        people = [(65, 100)]
        self.assertEqual(largest_tower(people).height, 1)

    def test_two_person_tower(self):
        people = [(65, 100), (55, 95)]
        self.assertEqual(largest_tower(people).height, 2)

    def test_many_people_1(self):
        people = [(100,60), (110, 55), (120, 70), (105, 65), (118, 70), (115, 75), (130, 80) ]
        self.assertEqual(largest_tower(people).height, 5)

    def test_many_people_2(self):
        people = [
            (65, 100), (70, 150), (56,90), (75, 190), (60, 95), (68, 110)
                ]
        self.assertEqual(largest_tower(people).height, 6)

    def test_many_people_3(self):
        people = [(50, 100), (60, 110), (70, 120), (80, 130)] 
        self.assertEqual(largest_tower(people).height, 4)

    def test_many_people_4(self):
        people = list(reversed([(50, 100), (60, 110), (70, 120), (80, 130)]))
        self.assertEqual(largest_tower(people).height, 4)

    def test_many_people_5(self):
        people = [(50, 100), (60, 90), (70, 80), (80, 70)]
        self.assertEqual(largest_tower(people).height, 1)


if __name__ == "__main__":
    unittest.main()
