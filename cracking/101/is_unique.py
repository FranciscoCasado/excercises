"""
Implement an algorithm to determine if a string has all unique characters. What if u cannot use additional data structures?
"""

def is_unique(str) -> bool :
    mem = []
    for char in str:
        if char in mem:
            return False
        mem.append(char)

    return True
