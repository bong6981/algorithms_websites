## https://www.acmicpc.net/problem/2253

def sol1():
    import heapq
    import sys
    sys.stdin = open("input.txt")
    input = sys.stdin.readline

    N, M = map(int, input().rstrip().split())
    board = [-1] * (N+1)

    for _ in range(M):
        board[int(input().rstrip())] = -2

    arr = []
    heapq.heappush(arr, (2, 1, 1)) #des, jump, cnt

    while arr:
        now = heapq.heappop(arr)

        if now[0] > N :
            break

        while len(arr) > 0 and arr[0][0] == now[0] and arr[0][1] == now[1]:
            heapq.heappop(arr)
        
        now, jump, cnt = now

        if board[now] == -2:
            continue

        if board[now] !=  -1:
            board[now] = min(board[now], cnt)
        
        else:
            board[now] = cnt
        
        if jump > 1:
            heapq.heappush(arr, (now+(jump-1), jump-1, cnt+1))
        heapq.heappush(arr,(now+jump, jump, cnt+1))
        heapq.heappush(arr,(now+jump+1, jump+1, cnt+1))
    
    print(board[N])


def sol_dp():
    import sys
    sys.stdin = open("input.txt")
    input = sys.stdin.readline

    N, M = map(int, input().rstrip().split())
    MAX_JUMP = int((2*N)**0.5)
    INF = int(1e9)

    dp = [[INF] * (MAX_JUMP+2) for _ in range(N+1)]
    stones = set()

    for _ in range(M):
        stones.add(int(input().rstrip()))

    dp[1][0] = 0

    for i in range(2, N+1):
        if i in stones:
            continue

        for j in range(1, int((2*i)**0.5+1)):
            dp[i][j] = min(dp[i-j][j-1], dp[i-j][j], dp[i-j][j+1]) + 1
    
    ans = min(dp[N])
    if ans == INF:
        print(-1)
    else:
        print(ans)
    


sol_dp()



