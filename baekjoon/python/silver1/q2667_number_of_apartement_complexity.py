# 3:47
import sys
input = sys.stdin.readline

N = int(input().rstrip())
graph = []
visited = [[0] * (N) for _ in range(N)]

for _ in range(N):
    graph.append(list(map(int, list(input().rstrip()))))

moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def dfs(x, y):
    visited[x][y] = 1
    cnt = 1
    for m in moves:
        nx = x + m[0]
        ny = y + m[1]
        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] == 1:
                if not visited[nx][ny]:
                    cnt += dfs(nx, ny)
    return cnt

num = 0
cnt = []
for i in range(N):
    for j in range(N):
        if graph[i][j]:
            if not visited[i][j]:
                num += 1
                cnt.append(dfs(i, j))

print(num)
cnt.sort()
for c in cnt:
    print(c)
