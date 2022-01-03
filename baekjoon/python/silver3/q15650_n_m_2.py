# https://www.acmicpc.net/problem/15650

from itertools import combinations

def solution():
    n, m = map(int, input().split())
    for c in combinations(list( str(i) for i in range(1, n+1)), m) :
        print(" ".join(sorted(list(c))))

solution()
