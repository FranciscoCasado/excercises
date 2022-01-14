import unittest

from cracking.ex_0702.call import CallSeverity
from cracking.ex_0702.employee import Employee, EmployeeRole, EmployeeFactory

class TestEmployee(unittest.TestCase):
    def test_create_employee(self):
        factory = EmployeeFactory()
        director = factory.create_employee("director")
        self.assertEqual(director.role, EmployeeRole.DIRECTOR)

        manager = factory.create_employee("manager")
        self.assertEqual(manager.role, EmployeeRole.MANAGER)

        respondent = factory.create_employee("respondent")
        self.assertEqual(respondent.role, EmployeeRole.RESPONDENT)


class TestCallSeverity(unittest.TestCase):
    def test_hierarchy(self):
        self.assertEqual(CallSeverity.DIRECTOR, EmployeeRole.DIRECTOR)
        self.assertEqual(CallSeverity.MANAGER, EmployeeRole.MANAGER)
        self.assertEqual(CallSeverity.RESPONDENT, EmployeeRole.RESPONDENT)

        self.assertGreater(CallSeverity.DIRECTOR, EmployeeRole.MANAGER)
        self.assertGreater(CallSeverity.DIRECTOR, EmployeeRole.RESPONDENT)
        self.assertGreater(CallSeverity.MANAGER, EmployeeRole.RESPONDENT)


if __name__ == "__main__":
    unittest.main()
