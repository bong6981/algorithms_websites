## https://www.acmicpc.net/problem/16234

from collections import deque
import sys
input = sys.stdin.readline 

def move(i, j, t):
    q = deque()
    q.append((i, j))
    union = [(i,j)]
    sum = board[i][j]
    visited[i][j] = t
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + moves_x[i]
            ny = y + moves_y[i]
            if(0<= nx < n) and (0<=ny<n):
                if visited[nx][ny] != t:
                    if l <= abs(board[x][y] - board[nx][ny]) <= r :
                        sum += board[nx][ny]
                        q.append((nx, ny))
                        visited[nx][ny] = t
                        union.append((nx, ny))
    if len(union) > 1:
        average = sum // len(union)
        for x, y in union :
            board[x][y] = average
            search.append((x, y))
        return 1
    return 0


n, l, r = map(int, input().split())
moves_x = [-1, 0, 1, 0]
moves_y = [0, 1, 0, -1]

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

t = 0
visited = [[-1 for _ in range(n)] for _ in range(n)]

search = deque()
for i in range(n):
    for j in range(n):
        search.append((i, j))

while True: 
    cnt = 0
    for _ in range(len(search)):
        i, j = search.popleft()
        if visited[i][j] != t:
            x = move(i, j, t)
            cnt += x
    if cnt == 0 :
        break
    t += 1

print(t)

                    
