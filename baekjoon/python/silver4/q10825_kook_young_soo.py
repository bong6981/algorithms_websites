## https://www.acmicpc.net/problem/10825

import sys
input = sys.stdin.readline

n = int(input())
result = []
for _ in range(n):
    name, kook, young, soo = input().split()
    kook = int(kook)
    young = int(young)
    soo = int(soo)
    result.append((kook, young, soo, name))

result.sort(key= lambda x : (-x[0], x[1], -x[2], x[3]))

for r in result:
    print(r[3])
