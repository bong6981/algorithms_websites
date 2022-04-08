# 11:38
# https://www.acmicpc.net/problem/11279

import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    order = int(input())
    if order == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr)[1])
    else:
        heapq.heappush(arr, (-order, order))
