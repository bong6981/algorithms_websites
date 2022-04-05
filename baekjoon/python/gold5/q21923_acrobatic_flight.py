import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(n)]


## 상승기류의 최대값 
ascending_points = [[0 for _ in range(m)] for _ in range(n)]
## 상승기류 포인트 초기화
ascending_points[n-1][0] = points[n-1][0]
for i in range(n-2, -1, -1):
    ascending_points[i][0] = points[i][0] + ascending_points[i+1][0]
for i in range(1, m):
    ascending_points[n-1][i] = points[n-1][i] + ascending_points[n-1][i-1]
for i in range(n-2, -1, -1):
    for j in range(1, m):
        ascending_points[i][j] = points[i][j] + max(ascending_points[i-1][j], ascending_points[i][j-1])

decending_points = [[-INF for _ in range(m)] for _ in range(n)]
decending_points[n-1][m-1] = points[n-1][m-1]
for i in range(n-2, -1, -1):
    decending_points[i][m-1] = points[i][m-1] + decending_points[i+1][m-1]
for i in range(m-2, -1, -1):
    decending_points[n-1][i] = points[n-1][i] + decending_points[n-1][i+1]
for i in range(n-2, -1, -1):
    for j in range(m-2, -1, -1):
        decending_points[i][j] = points[i][j] + max(decending_points[i+1][j], decending_points[i][j+1])

answer = -INF
for i in range(n):
    for j in range(m):
        answer = max(answer, ascending_points[i][j] + decending_points[i][j])

print(answer)

