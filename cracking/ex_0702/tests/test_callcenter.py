import unittest

from cracking.ex_0702.callcenter import CallCenter, Call, CallSeverity


class TestCallCenter(unittest.TestCase):
    def test_create_call_center(self):
        personel = {
            "respondent": 20,
            "manager": 5,
            "director": 2
        }

        call_center = CallCenter(personel)

        self.assertEqual(len(call_center._available["director"]), 2)
        self.assertEqual(len(call_center._available["manager"]), 5)
        self.assertEqual(len(call_center._available["respondent"]), 20)
        self.assertEqual(len(call_center._busy), 0)

    def test_assign_call_to_respondent(self):
        call = Call(CallSeverity.RESPONDENT)

        personel = {
            "respondent": 1,
            "manager": 1,
            "director": 1
        }
        
        call_center = CallCenter(personel)
        
        call_center.assign_call(call)
        self.assertEqual(len(call_center._available["respondent"]), 0)
        self.assertEqual(len(call_center._available["manager"]), 1)
        self.assertEqual(len(call_center._available["director"]), 1)
        self.assertEqual(len(call_center._busy), 1)

    
    def test_assign_call_to_manager(self):
        call = Call(CallSeverity.MANAGER)

        personel = {
            "respondent": 1,
            "manager": 1,
            "director": 1
        }
        
        call_center = CallCenter(personel)
        
        call_center.assign_call(call)
        self.assertEqual(len(call_center._available["respondent"]), 1)
        self.assertEqual(len(call_center._available["manager"]), 0)
        self.assertEqual(len(call_center._available["director"]), 1)
        self.assertEqual(len(call_center._busy), 1)

    def test_assign_call_to_director(self):
        call = Call(CallSeverity.DIRECTOR)

        personel = {
            "respondent": 1,
            "manager": 1,
            "director": 1
        }
        
        call_center = CallCenter(personel)
        
        call_center.assign_call(call)
        self.assertEqual(len(call_center._available["respondent"]), 1)
        self.assertEqual(len(call_center._available["manager"]), 1)
        self.assertEqual(len(call_center._available["director"]), 0)
        self.assertEqual(len(call_center._busy), 1)


if __name__ == "__main__":
    unittest.main()
        