import unittest

from callcenter import CallCenter


class TestCallCenter(unittest.TestCase):
    def test_create_call_center(self):
        personel = {
            "director": 2,
            "manager": 5,
            "respondent": 20
        }

        call_center = CallCenter(personel)

        self.assertEqual(len(call_center._director_queue), 2)
        self.assertEqual(len(call_center._manager_queue), 5)
        self.assertEqual(len(call_center._respondent_queue), 20)
        self.assertEqual(len(call_center._busy_people), 0)


if __name__ == "__main__":
    unittest.main()
        