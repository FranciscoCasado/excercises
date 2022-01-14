from .ordered_enum import OrderedEnum

class Call:
    def __init__(self, severity):
        self._severity = severity

    @property
    def severity(self):
        return self._severity


class CallSeverity(OrderedEnum):
    DIRECTOR = 2
    MANAGER = 1
    RESPONDENT =0
