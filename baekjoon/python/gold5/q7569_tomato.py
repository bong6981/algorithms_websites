## https://www.acmicpc.net/problem/7569
from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().rstrip().split())
graph = []
cnt = 0
ripe = []
for k in range(H):
    box = []
    for i in range(N):
        row = list(map(int, list(input().rstrip().split())))
        box.append(row)
        for j in range(M):
            if row[j] == 1: ## 익은 
                ripe.append((k, i, j))
                cnt += 1
            elif row[j] == 0: ## 익지 않은
                cnt += 1
    graph.append(box)
moves = [(-1, 0, 0), (1, 0, 0), (0, 0, -1), (0, 0, 1), (0, 1, 0), (0, -1, 0)]

if cnt == len(ripe):
    print(0)

else:
    day = 0
    que = deque()
    for r_to in ripe:
        que.append((0,r_to))
    
    ripe_cnt = len(ripe)
    all_ripe = False
    while que:
        now, pos = que.popleft()
        k, i, j = pos
        for ki, ii, ji in moves:
            nk = k + ki
            ni = i + ii
            nj = j + ji
            if 0 <= nk < H and 0 <= ni < N and 0 <= nj < M:
                if graph[nk][ni][nj] == 0:
                    graph[nk][ni][nj] = 1
                    que.append((now + 1, (nk, ni, nj)))
                    ripe_cnt += 1
                    if ripe_cnt == cnt:
                        print(now+1)
                        all_ripe = True
                        break
        if all_ripe:
            break
    if not all_ripe:
        print(-1)
        
        
        
    



