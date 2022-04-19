## https://www.acmicpc.net/problem/1432
import heapq
import sys
input = sys.stdin.readline
N = int(input().rstrip())

graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for i in range(1, N+1):
    for j, c in enumerate(input().rstrip(), 1):
        if int(c) == 1:
            graph[j].append(i)
            indegree[i] += 1

q = []
for i, v in enumerate(indegree[1:], 1):
    if v == 0:
        heapq.heappush(q, -i)

order = []
while q:
    now = -heapq.heappop(q)
    order.append(now)
    for des in graph[now]:
        indegree[des] -= 1
        if indegree[des] == 0:
            heapq.heappush(q, -des)

if len(order) < N :
    print(-1)
else:
    ans = [0] * (N+1)
    for i, v in enumerate(order, 1):
        ans[v] = (N+1) - i
    print(*ans[1:])

