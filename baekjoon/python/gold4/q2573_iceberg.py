## https://www.acmicpc.net/problem/2573
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N, M = map(int, input().split())

ground = [list(map(int, input().split())) for _ in range(N)]
ads = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
def dfs(x, y, visited, melt):
    visited[x][y] = 1
    cnt = 0
    for ad in ads:
        nx = x + ad[0]
        ny = y + ad[1]
        if not visited[nx][ny]:
            if not ground[nx][ny] :
                cnt +=1
            else:
                melt = dfs(nx, ny, visited, melt)
    if cnt:
        melt.append(((x, y), cnt))
    return melt

def sol():
    global ground
    time = 0
    while True:
        visited = [[0] * M for _ in range(N)]

        cnt = 0
        melt = []
        for i in range(1, N-1):
            for j in range(1, M-1):
                if ground[i][j] and not visited[i][j]:
                    if cnt > 0:
                        print(time)
                        return
                    cnt += 1
                    melt = dfs(i, j, visited, melt)
        
        if len(melt) != 0:
            for pos, to_melt in melt:
                x, y = pos
                ground[x][y] = max(0, ground[x][y] - to_melt)
        
        if cnt == 0:
            print(0)
            return
        
        if cnt >= 2:
            print(time)
            return
        
        time += 1


sol()






