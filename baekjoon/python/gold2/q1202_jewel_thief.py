## https://www.acmicpc.net/problem/1202
from collections import deque
import heapq
import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

items = []
for _ in range(N):
    M, V = map(int, input().rstrip().split())
    items.append((M, V))

items.sort()
items = deque(items)
bags = []
for _ in range(K):
    bags.append(int(input().rstrip()))

bags.sort()

ans = 0
acc = []
for bag in bags:
    
    while items:
        if items[0][0] <= bag:
            m, v =items.popleft()
            heapq.heappush(acc, -v)
        else:
            break
    
    if acc:
        ans += -heapq.heappop(acc)
    

print(ans)
