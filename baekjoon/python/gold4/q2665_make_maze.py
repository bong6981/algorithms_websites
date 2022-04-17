## https://www.acmicpc.net/problem/2665
import heapq
import sys

input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, list(input().rstrip()))))

MAX_D = 251
dis_g = [[MAX_D] * N for _ in range(N)]

dis_g[0][0] = 0 
q = [(0, (0, 0))]

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while q:
    dist, pos = heapq.heappop(q)
    x, y =  pos
    if dis_g[x][y] < dist:
        continue
    for xi, yi in moves:
        nx = x + xi
        ny = y + yi
        if 0 <= nx < N and 0 <= ny < N:
            cost = dist + (not (graph[nx][ny]))
            if cost < dis_g[nx][ny]:
                dis_g[nx][ny] = cost
                q.append((cost, (nx, ny)))

print(dis_g[N-1][N-1])
