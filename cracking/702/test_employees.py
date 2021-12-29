import unittest

from call import CallSeverity
from employee import Employee, EmployeeRole, Director, Manager, Respondent

class TestEmployee(unittest.TestCase):
    def test_create_employee(self):       
        director = Director()
        self.assertEqual(director.role, EmployeeRole.DIRECTOR)

        manager = Manager()
        self.assertEqual(manager.role, EmployeeRole.MANAGER)

        respondent = Respondent()
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
