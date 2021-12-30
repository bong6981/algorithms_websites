# https://www.acmicpc.net/problem/4485
import heapq

INF = int(1e9)
def solution():
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    idx = 1

    while True:
        n = int(input())
        if n == 0 :
            break

        board = []
        for _ in range(n):
            board.append(list(map(int, input().split())))
        
        dp = [[INF] * n for _ in range(n)]
        dp[0][0] = board[0][0]

        q = []
        heapq.heappush(q, (dp[0][0], 0, 0))
        while q :
            r, x, y = heapq.heappop(q)
            if dp[x][y] < r :
                continue
            for m in moves :
                nx = x + m[0]
                ny = y + m[1]
                if 0 <= nx < n and 0 <= ny < n :
                    cost = r + board[nx][ny]
                    if cost < dp[nx][ny]:
                        dp[nx][ny] = cost
                        heapq.heappush(q, (cost, nx, ny))

        print("Problem "+ str(idx) + ": " + str(dp[n-1][n-1]))
        idx += 1            

solution()
