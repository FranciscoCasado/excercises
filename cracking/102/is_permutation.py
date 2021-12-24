"""
Given two Strigns, write a method to decide if one is a permutaion of the other
"""


def is_permutation(str1, str2) -> bool:
    return sorted(str1) == sorted(str2)


def is_permutation_without_strcmp(str1, str2) -> bool:
    # First check length
    if len(str1) != len(str2):
        return False

    char_table = dict()

    for c in str1:
        if c in char_table.keys():
            char_table[c] += 1
        else:
            char_table[c] = 1

    for c in str2:
        if c in char_table.keys():
            char_table[c] += 1
        else:
            return False

    sum = 0
    for value in char_table.values():
        sum += value

    return sum % 2 == 0


"""
Alternatives: 
- Instead of checking even sum, the first string could increase the counter while the second string decreases it
- First check str lengths. If equal, sum all characters (as ints, using ord()) from the first string, then subtract every character of the second string. If result is equal to zero, both strings are permutations :)
"""
