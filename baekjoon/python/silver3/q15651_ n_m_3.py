## https://www.acmicpc.net/problem/15651
from itertools import product

n, m = map(int, input().split())

data = list(range(1, n+1))
ans = product(data, repeat=m)
for a in ans:
    for b in a :
        print(b, end=" ")
    print()
