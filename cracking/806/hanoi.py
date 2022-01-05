from collections import deque


class Tower:
    def __init__(self, n=0):
        self._list = deque([n - i for i in range(n)])

    @property
    def is_empty(self):
        return not self._list

    def pop(self):
        if not self._list:
            return None
        return self._list.pop()

    def push(self, i):
        if type(i) != int:
            raise HanoiDiscError("disc must be an integer")
        if not self.is_empty:
            if i > self._list[-1]:
                raise HanoiDiscError("disc too big for this tower")
        self._list.append(i)

    def __repr__(self):
        return str(list(self._list))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._list == other._list

        return False


class HanoiDiscError(Exception):
    pass


class MoveTowerError(Exception):
    pass



class HanoiTowers:
    def __init__(self, n=0):
        self._towers = [Tower(n)]
        self._towers.append(Tower())
        self._towers.append(Tower())
        self._n = n

    def shift_towers(self):
        A = self._towers[0]
        B = self._towers[1]
        C = self._towers[2]
        self._move_tower(A, B, C, self._n)

    def _move_tower(self, src, dest, aux, n=1):
        if n <= 0:
            raise MoveTowerError("amount of discs to be moved must be greater than zero")
        if src.is_empty:
            raise MoveTowerError("src tower is empty and cannot be moved")
        if n == 1:
            dest.push(src.pop())
            return

        self._move_tower(src, aux, dest, n - 1)
        dest.push(src.pop())
        self._move_tower(aux, dest, src, n - 1)

    def __repr__(self):
        a = "A:" + repr(self._towers[0])
        b = "\nB:" + repr(self._towers[1])
        c = "\nC:" + repr(self._towers[2])
        return a + b + c
