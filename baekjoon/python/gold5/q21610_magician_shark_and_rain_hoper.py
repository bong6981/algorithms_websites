#https://www.acmicpc.net/problem/21610

import sys
input = sys.stdin.readline

def solution():
    moves = [(), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
    n, m = map(int, input().split())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    clouds = [(n-2, 0), (n-2, 1), (n-1, 0), (n-1, 1)]
    for _ in range(m):
        d, s = map(int, input().split())
        movex = moves[d][0]
        movey = moves[d][1]
        disappeared_clouds = []
        for cloud in clouds:
            nx = cloud[0] + (movex * s)
            ny = cloud[1] + (movey * s)
            if nx < 0 :
                nx = n - ((-nx) % n)
                if nx == n :
                    nx = 0
            if nx >= n :
                nx = nx % n
            if ny < 0 :
                ny = n - ((-ny) % n)
                if ny == n :
                    ny = 0
            if ny >= n :
                ny = (ny) % n 
            board[nx][ny] += 1
            disappeared_clouds.append((nx, ny))
        clouds = []
        for cloud in disappeared_clouds :
            x = cloud[0]
            y = cloud[1]
            cnt = 0
            for move in [moves[2], moves[4], moves[6], moves[8]] :
                nx = x + move[0]
                ny = y + move[1]
                if 0 <= nx < n and 0 <= ny < n :
                    if board[nx][ny] >= 1:
                        cnt += 1
            board[x][y] += cnt
        for i in range(n):
            for j in range(n):
                if (i, j) in disappeared_clouds : 
                    continue
                if board[i][j] >= 2 :
                    board[i][j] -= 2
                    clouds.append((i, j))
    result = 0
    for i in board :
        result += sum(i)
    return result

# print(solution())





    
            



