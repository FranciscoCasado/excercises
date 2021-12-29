import unittest

from callcenter import CallCenter, Call, CallSeverity


class TestCallCenter(unittest.TestCase):
    def test_create_call_center(self):
        personel = {
            "director": 2,
            "manager": 5,
            "respondent": 20
        }
        severity_list = ["respondent", "manager", "director"]

        call_center = CallCenter(personel, severity_list)

        self.assertEqual(len(call_center._available["director"]), 2)
        self.assertEqual(len(call_center._available["manager"]), 5)
        self.assertEqual(len(call_center._available["respondent"]), 20)
        self.assertEqual(len(call_center._busy), 0)

    def test_assign_call_to_respondent(self):
        call = Call(CallSeverity.RESPONDENT)

        personel = {
            "director": 1,
            "manager": 1,
            "respondent": 1
        }
        severity_list = ["respondent", "manager", "director"]
        
        call_center = CallCenter(personel, severity_list)
        
        call_center.assign_call(call)
        self.assertEqual(len(call_center._available["respondent"]), 0)
        self.assertEqual(len(call_center._busy), 1)


if __name__ == "__main__":
    unittest.main()
        