## https://www.acmicpc.net/problem/1916
import heapq
import sys

input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, des, cost = map(int, input().rstrip().split())
    graph[start].append((cost, des))

S, E = map(int, input().rstrip().split())

MAX_D = (10 ** 5) * (10 ** 5) + 1
que = [(0, S)]
cost_g = [MAX_D] * (N+1) 
cost_g[S] = 0
while que:
    dis, now = heapq.heappop(que)
    if cost_g[now] < dis:
        continue
    for des in graph[now]:
        cost = des[0] + dis
        if cost < cost_g[des[1]]:
            cost_g[des[1]] = cost
            heapq.heappush(que, (cost, des[1]))
print(cost_g[E])

