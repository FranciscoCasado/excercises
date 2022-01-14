from abc import ABC, abstractmethod, abstractproperty

from .ordered_enum import OrderedEnum
from .call import Call

class Employee(ABC):
    def __init__(self, role=None):
        self._role = role
        self._busy = False

    @property
    def role(self):
        return self._role

    @property
    def is_busy(self):
        return self._busy

    def handle_call(self, call):
        if call.severity <= self._role:
            self._busy = True
            return True
        
        return False
    

class EmployeeRole(OrderedEnum):
    DIRECTOR = 2
    MANAGER = 1
    RESPONDENT = 0

    

class Director(Employee):
    def __init__(self):
        Employee.__init__(self, role=EmployeeRole.DIRECTOR)

class Manager(Employee):
    def __init__(self):
        Employee.__init__(self, role=EmployeeRole.MANAGER)


class Respondent(Employee):
    def __init__(self):
        Employee.__init__(self, role=EmployeeRole.RESPONDENT)


class EmployeeFactory:

    PRODUCT = {
        "director": Director,
        "manager": Manager,
        "respondent": Respondent,
    }

    def create_employee(self, role) -> Employee:
        if role in self.PRODUCT:
            return self.PRODUCT[role]()
        raise FactoryProductError(f"There is no '{role}' role in our inventory")

class FactoryProductError(Exception):
    pass