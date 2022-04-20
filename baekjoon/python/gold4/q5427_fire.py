## https://www.acmicpc.net/problem/5427
from collections import deque
import sys

input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    w, h = map(int, input().rstrip().split())

    ## 빈공간:0, 벽-1: 불:1
    graph = [[0] * w for _ in range(h)]
    moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    visited = set()

    start = (0, 0)
    fires = []

    for i in range(h):
        row = list(input().rstrip())
        for j in range(w):
            if row[j] == '#':
                graph[i][j] = -1
            elif row[j] == '*':
                fires.append((i, j))
                graph[i][j] = 1
            elif row[j] == "@":
                start = (i, j)

    def spred_fire(fires):
        global graph
        new_fires = []
        for x, y in fires:
            for move in moves:
                nx = x + move[0]
                ny = y + move[1]
                if 0 <= nx < h and 0 <= ny < w:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = 1
                        new_fires.append((nx, ny))
        return new_fires

        

    # 상근 탈출 
    q = deque([(0, start)])
    escape = False
    now = 0
    while q:
        time, pos = q.popleft()
        x, y = pos

        if now == time:
            fires = spred_fire(fires)
            now += 1

        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            next = time + 1
            if not (0 <= nx < h and 0 <= ny < w):
                print(next)
                escape = True
                break
            else:
                if graph[nx][ny] == -1 : continue
                if graph[nx][ny] == 1: continue
                if (nx, ny) not in visited:
                    q.append((next, (nx, ny)))
                    visited.add((nx, ny))
        if escape:
            break
    if not escape:
        print("IMPOSSIBLE")
