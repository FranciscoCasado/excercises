

def is_permutation(str1, str2) -> bool:
    # First check length
    if len(str1) != len(str2):
        return False
    
    char_table = dict()

    for c in (str1):
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
    
    return ( sum % 2 == 0 ) 
