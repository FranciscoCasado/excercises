


def move_tower(src, dest, aux, n):
    if n == 1:
        dest.append(src.pop())
        return

    move_tower(src, aux, dest, n-1)
    dest.append(src.pop())
    move_tower(aux, dest, src, n-1)


if __name__ == "__main__":
    N = 10
    A = [N-i for i in range(N)]
    B = []
    C = []

    move_tower(A,B,C,N)
    print(A)
    print(B)
    print(C)
