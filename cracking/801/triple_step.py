def count_ways(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    return count_ways(n - 1) + count_ways(n - 2) + count_ways(n - 3)


def count_ways_dynamic(n):
    s = [0, 1, 2]

    for i in range(3, n + 1):
        s.append(s[i - 1] + s[i - 2] + s[i - 3])

    return s[n]
