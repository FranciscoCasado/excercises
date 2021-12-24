"""
Implement an algorithm to determine if a string has all unique characters. What if u cannot use additional data structures?
"""


def is_unique_brute_force(str) -> bool:
    mem = []
    for char in str:
        if char in mem:
            return False
        mem.append(char)

    return True


def is_unique(str) -> bool:
    bit_vector = 0b0
    for char in str:
        char_index = ord(char) - 97
        if (bit_vector >> char_index) & 1:
            return False
        bit_vector |= 1 << char_index
    return True
