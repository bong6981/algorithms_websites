h_moves = [(-2, -1), (-2, 1), (-1,-2), (-1,2), (1, -2), (1, 2), (2, 1), (2, -1)]
m_moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]


## k번만 h / 

import sys
input = sys.stdin.readline

K = int(input())
W, H = map(int, input().split())
graph = []
for _ in range(H):
    graph.append(list(map(int, input().split())))

visited = [[[0 for _ in range(W)] for _ in range(H)] for _ in range(K+1)]
ans = -1
print("====================")
def move(cnt, r, c, h_cnt):
    global ans
    global visited
    # print(r, c, cnt, visited[h_cnt][r][c], h_cnt)
    if(r==1 and c == 2):
        print("@@@@@@@@@2")
        print(cnt, r, c, h_cnt)
    if visited[h_cnt][r][c]:
        return
    
    visited[h_cnt][r][c] = 1
    
    if r == H-1 and c == W-1:
        if ans == -1 or ans > cnt:
            ans = cnt
        return

    if h_cnt > 0:
        for h_m in h_moves:
            nr = r + h_m[0]
            nc = c + h_m[1]
            if 0 <= nr < H and 0 <= nc < W:
                if graph[nr][nc] != 1:
                    move(cnt+1, nr, nc, h_cnt-1)
    

        
    # if(r==0 and c == 0):
    #     if h_cnt > 0:
    #         for h_m in h_moves:
    #             nr = r + h_m[0]
    #             nc = c + h_m[1]
    #             if 0 <= nr < H and 0 <= nc < W:
    #                 if graph[nr][nc] != 1:
    #                     print(cnt+1, nr, nc, h_cnt-1)

        
    if(r==1 and c == 2):
        for m_m in m_moves:
            nr = r + m_m[0]
            nc = c + m_m[1]
            print(cnt+1, nr, nc, h_cnt)
            print("********")
            if 0 <= nr < H and 0 <= nc < W:
                if graph[nr][nc] != 1:
                    print(cnt+1, nr, nc, h_cnt)
    for m_m in m_moves:
        nr = r + m_m[0]
        nc = c + m_m[1]
        if 0 <= nr < H and 0 <= nc < W:
            if graph[nr][nc] != 1:
                move(cnt+1, nr, nc, h_cnt)
 



move(0, 0, 0, K)
print(ans)


