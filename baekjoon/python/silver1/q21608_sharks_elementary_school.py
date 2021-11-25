## https://www.acmicpc.net/problem/21608
def solution():
    n = int(input())
    board = [[0] * n for _ in range(n)]
    move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    like_data = [[] for _ in range(n**2+1)]
    for _ in range(n**2):
        next_x = -1
        next_y = -1
        data = list(map(int, input().split()))
        s = data[0]
        like_data[s] = data
        like = data[1:]
        candidate = []
        like_number = 0
        for i in range(n):
            for j in range(n):
                if board[i][j] == 0:
                    cnt = 0
                    for k in range(4):
                        nx = i+move[k][0]
                        ny = j+move[k][1]
                        if 0<= nx < n and 0 <= ny < n:
                            if board[nx][ny] in like:
                                cnt += 1
                    if cnt == like_number :
                        candidate.append((i, j))
                    elif cnt > like_number :
                        candidate = [(i, j)]
                        like_number = cnt
        if len(candidate) > 1 : 
            new_candidates = []
            adjacent_emty = 0
            for can in candidate:
                i = can[0]
                j = can[1]
                cnt = 0
                for k in range(4):
                        nx = i+move[k][0]
                        ny = j+move[k][1]
                        if 0<= nx < n and 0 <= ny < n:
                            if board[nx][ny] == 0 :
                                cnt += 1
                if cnt == adjacent_emty :
                    new_candidates.append((i, j))
                elif cnt > adjacent_emty:
                    new_candidates = [(i, j)]
                    adjacent_emty = cnt
            candidate = new_candidates
            if len(candidate) > 1:
                candidate.sort()
        next_x = candidate[0][0]
        next_y = candidate[0][1]
        board[next_x][next_y] = s

        statisfaction = 0
        for i in range(n):
            for j in range(n):
                x = board[i][j]
                cnt = 0
                for k in range(4):
                    nx = i+move[k][0]
                    ny = j+move[k][1]
                    if 0<= nx < n and 0 <= ny < n:
                        if board[nx][ny] in like_data[x] :
                            cnt += 1
                if cnt != 0:
                    statisfaction += 10 ** (cnt-1)
        
    return statisfaction    

print(solution())

## 파이썬 랭커 id: jh05013 님의 풀이 
def other():
    n = int(input())
    grid = [[None]*n for i in range(n)]
    likes = [[] for i in range(n**2+1)]
    for ITER in range(n**2):
        no, *like = map(int,input().split())
        likes[no] = like
        ans = (9999, 9999, -1, -1) # -like, -emp, i, j
        for i in range(n):
            for j in range(n):
                if grid[i][j]: continue
                l0 = emp0 = 0
                for ni,nj in (i-1,j),(i+1,j),(i,j-1),(i,j+1):
                    if not (0<=ni<n and 0<=nj<n): continue
                    if grid[ni][nj] == None: emp0+= 1
                    elif grid[ni][nj] in like: l0+= 1
                ans = min(ans, (-l0, -emp0, i, j))
        _, __, i, j = ans
        grid[i][j] = no

    ans = 0
    for i in range(n):
        for j in range(n):
            like = likes[grid[i][j]]
            l0 = 0
            for ni,nj in (i-1,j),(i+1,j),(i,j-1),(i,j+1):
                if 0<=ni<n and 0<=nj<n and grid[ni][nj] in like: l0+= 1
            ans+= [0, 1, 10, 100, 1000][l0]
    print(ans)

print(other())
