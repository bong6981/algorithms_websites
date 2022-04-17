from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

que = deque([(0,0)])

while que:
    x, y = que.popleft()
    for m in moves:
        nx = x + m[0]
        ny = y + m[1]
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny]:
                if graph[nx][ny] == 1 or graph[x][y] + 1 < graph[nx][ny]:
                    graph[nx][ny] = graph[x][y] + 1
                    que.append((nx, ny))
print(graph[N-1][M-1])



