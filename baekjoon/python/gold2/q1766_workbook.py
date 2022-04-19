## https://www.acmicpc.net/problem/1766
import sys
input = sys.stdin.readline


N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
    A, B =  map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

import heapq
q = []
for i in range(N+1):
    if indegree[i] == 0:
        heapq.heappush(q, i)

result = []
while q:
    now = heapq.heappop(q)
    result.append(now)
    for des in graph[now]:
        indegree[des] -= 1
        if indegree[des] == 0:
            heapq.heappush(q, des)

print(*result[1:])


    
