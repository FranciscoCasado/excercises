from enum import Enum


class OrderedEnum(Enum):
    def __gt__(self, other):
        return self.value > other.value

    def __geq__(self, other):
        return self.value >= other.value

    def __lt__(self, other):
        return self.value < other.value

    def __leq__(self, other):
        return self.value <= other.value

    def __eq__(self, other):
        return self.value == other.value
