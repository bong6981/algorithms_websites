# https://www.acmicpc.net/problem/3055

from collections import deque
import sys

input = sys.stdin.readline

R, C  = map(int, input().split())
graph = [[0] * C for _ in range(R)]

start = None
water = []

for j in range(R):
    row = list(input().rstrip())
    for i in range(C):
        if row[i] == 'D':
            graph[j][i] = -2
        elif row[i] == '*':
            graph[j][i] = -1
            water.append((j, i))
        elif row[i] == 'S':
            start = (j, i)
        elif row[i] == 'X':
            graph[j][i] = -3

que = deque([(0, start)])
moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def spill(water):
    global graph
    new_water = []
    for x, y in water:
        for xi, yi in moves :
            nx = x + xi
            ny = y + yi
            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] >= 0:
                    graph[nx][ny] = -1
                    new_water.append((nx, ny))
    water.extend(new_water)
    return water


next_time = 0
found = False
while que:
    now, pos = que.popleft()
    x, y = pos
    if now == next_time:
        next_time += 1
        water = spill(water)
    for xi, yi in moves :
        nx = x + xi
        ny = y + yi
        if 0 <= nx < R and 0 <= ny < C:
            cost = now + 1
            if graph[nx][ny] == -2:
                print(cost)
                found = True
                break ## 다른 사람들은 여기서 어떻게 했나. break -> break 
            if graph[nx][ny] == 0: ## 0말고 다른 숫자 넣어야 할 수도 
                graph[nx][ny] = cost
                que.append((cost, (nx, ny)))
    if found:
        break

if not found:
    print("KAKTUS")





        


