

def power_set(set: list) -> list:
    pow = [[]]
    for element in set:
        dup = duplicate_list_elements(pow)
        for d in dup:
            d.append(element)
            pow.append(d)


    return pow

def duplicate_list_elements(set: list) -> list:
    return [e.copy() for e in set]
