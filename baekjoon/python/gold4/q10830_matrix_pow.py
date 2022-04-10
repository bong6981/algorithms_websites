## https://www.acmicpc.net/problem/10830

import sys
input = sys.stdin.readline

import copy

n, b = map(int, input().split())
ord = [[0] * n for _ in range(n)]

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        ord[i][j] = row[j]

now = copy.deepcopy(ord)

def pow_n(now, n):
    if n == 1:
        return now
    if n == 2:
        return mul(now, now)

    half = pow_n(now, n//2)
    result = mul(half, half)
    if n % 2 == 1:
        result = mul(result, ord)
    return result


def mul(x, y):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res = 0
            for k in range(n):
                res += (x[i][k] * y[k][j])  % 1000
            result[i][j] = res % 1000
    return result


ans = pow_n(now, b)
for row in ans:
    for val in row:
        print(val % 1000, end=" ")
    print()



            


