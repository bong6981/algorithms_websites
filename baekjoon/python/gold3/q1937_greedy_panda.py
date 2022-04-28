## https://www.acmicpc.net/problem/1937
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input().rstrip())
forest = [[ ] for _ in range(N)]

for i in range(N):
    forest[i] = list(map(int, input().rstrip().split()))

moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]

acc = [[-1] * N for _ in range(N)]

def go(start):
    x, y = start
    if acc[x][y] != -1:
        return acc[x][y]

    cnt = 1
    for m in moves:
        nx = x + m[0]
        ny = y + m[1]
        if 0 <= nx < N and 0 <= ny < N:
            if forest[nx][ny] > forest[x][y]:
                result = go((nx, ny))
                cnt = max(result+1, cnt) 
    acc[x][y] = cnt
    return cnt


ans = 0
for i in range(N):
    for j in range(N):
        result = 0
        if acc[i][j] == -1:
            result = go((i, j))
        else:
            result = acc[i][j]
        ans = max(result, ans) 

print(ans)       
