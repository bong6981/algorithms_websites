# https://www.acmicpc.net/submit/3190
from cmath import pi
import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
k = int(input())
graph = [[0] * (n+2) for _ in range(n+2)]
# snake = 2
# apple = 1
# wall = -1
for i in [0, n+1]:
    for j in range(0, n+2):
        graph[i][j] = -1
    for z in range(0, n+2):
        graph[z][i] = -1

for _ in range(k):
    r, c = map(int, input().split())
    graph[r][c] = 1


l = int(input())
dir_info = [0] * ((10**4)+1)

for _ in range(l):
    sec, d = input().split()
    if d == "D":
        d = 1
    else:
        d = -1
    dir_info[int(sec)] = d

graph[1][1] = 2
moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
snake = deque([(1, 1)])

time = 0
d = 0
while len(snake) != 0 :
    for i in graph:
        print(i)
    x, y = snake[-1]
    time += 1
    nx = x + moves[d][0]
    ny = y + moves[d][1]

    if graph[nx][ny] == -1  or graph[nx][ny] == 2:
        break

    if graph[nx][ny] != 1 :
        del_x, del_y = snake.popleft()
        graph[del_x][del_y] = 0 
    
    graph[nx][ny] = 2
    snake.append((nx, ny))

    # 이동한 후에 방향 확인
    if dir_info[time] != 0:
        d += dir_info[time]
        if d == 4:
            d = 0
        elif d == -1:
            d = 3

print(time)
    
