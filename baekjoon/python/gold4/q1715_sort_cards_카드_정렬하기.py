## https://www.acmicpc.net/problem/1715

import heapq
import sys
input = sys.stdin.readline

n = int(input())
cards = []
for i in range(n):
    heapq.heappush(cards, int(input()))

ans = 0
while len(cards) > 1:
    c1 = heapq.heappop(cards)
    c2 = heapq.heappop(cards)
    heapq.heappush(cards, (c1+c2))
    ans += c1 + c2

print(ans)

