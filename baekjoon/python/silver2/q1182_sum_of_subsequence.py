## https://www.acmicpc.net/problem/1182

import sys
input = sys.stdin.readline

from itertools import combinations

n, s = map(int, input().split())
numbers = list(map(int, input().split()))
ans = 0

for i in range(1, n+1):
    for c in combinations(numbers, i) :
        if sum(list(c)) == s :
            ans += 1

print(ans)



