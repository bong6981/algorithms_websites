# https://www.acmicpc.net/problem/18352

from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().rstrip().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().rstrip().split())
    graph[A].append(B)

que = deque([(X, 0)])
dis = [-1] * (N+1)
dis[X] = 0
while que:
    now, cost = que.popleft()
    for des in graph[now]:
        if dis[des] == -1:
            dis[des] = cost + 1
            que.append((des, cost+1))

found = False
for i, v in enumerate(dis[2:], 2):
    if v == K:
        print(i)
        found = True
if not found:
    print(-1)

