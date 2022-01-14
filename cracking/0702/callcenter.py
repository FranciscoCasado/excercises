import logging

from employee import EmployeeFactory
from call import Call, CallSeverity

class CallCenter:
    def __init__(self, personel):

        factory = EmployeeFactory()
        self._available = { role: [factory.create_employee(role) for i in range(personel[role])]
                                    for role in personel}
                
        self._busy = []

    def assign_call(self, call):
        for role in self._available:
            if self._available[role]:
                employee = self._available[role][-1]
                
                if employee.handle_call(call):
                    logging.info(f"assigning call to {role}")
                    self._busy.append(self._available[role].pop())
                    return True

        logging.warning("All of our agents are busy, please hold the line or try again later")
        return None

            

        

