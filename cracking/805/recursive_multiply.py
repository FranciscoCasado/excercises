

def multiply(a, b):
    if b == 0:
        return 0

    if (b & 0b1):
        return multiply(a, (b-1)) + a

    return multiply(a << 1, b>>1)