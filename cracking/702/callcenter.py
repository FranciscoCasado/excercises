from employee import EmployeeFactory
from call import Call, CallSeverity

class CallCenter:
    def __init__(self, personel, severity_list):
        self._role_hierarchy = severity_list

        factory = EmployeeFactory()
        self._available = { role: [factory.create_employee(role) for i in range(personel[role])]
                                    for role in personel}
                
        self._busy = []

    def assign_call(self, call):
        role = self.who_is_available()
        if not role:
            print("All of our agents are busy, please hold the line or try again later")

        employee = self._available[role][-1]
        if employee.handle_call(call):
            print(f"assigning call to {role}")
            self._busy.append(self._available[role].pop())
        

    def who_is_available(self):
        for role in self._role_hierarchy:
            if self._available[role]:
                return role
        
        return None

            

        

