

def power_set(set: list) -> list:
    pow = [[]]
    for element in set:
        dup = [e.copy() for e in pow]
        for d in dup:
            d.append(element)
            pow.append(d)

    return pow
