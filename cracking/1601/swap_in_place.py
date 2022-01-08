

def swap(a, b):
    a = a - b
    b = b + a
    a = b - a
    return a, b

#TODO
def swap_bitwse(a, b):
    "Use xor (^) operator to swap two data in place"
    return a, b