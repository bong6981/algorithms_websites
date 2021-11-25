def solution():
    a, b, c, m = map(int, input().split())
    w = 0
    f = 0
    if a > m :
        return 0
    for _ in range(24):
        if f + a <= m : 
            f += a
            w += b
        else:
            if f < c:
                f = 0
            else:
                f -= c
    return w

print(solution())
