def add(a: int, b: int):
    # Python allocates ints in 4 bytes!
    s = 0  # sum
    c = 0  # carry
    for i in range(32):
        value = bit_sum(bit(a, i), bit(b, i), c)
        s = set_bit(s, value, i)
        c = carry(bit(a, i), bit(b, i), c)
    return s


def bit(a: int, index: int) -> bool:
    return (a >> index) & 1


def bit_sum(a: int, b: int, c: int) -> bool:
    return a ^ b ^ c


def carry(a: int, b: int, c: int) -> bool:
    return (a & b & c) ^ (a & b & (not c)) ^ ((not a) & b & c) ^ (a & (not b) & c)


def set_bit(a: int, value: int, index: int) -> int:
    if value < 0 or value > 1:
        raise ValueError("value must be either 0 or 1")
    return int(a | int(value << index))
