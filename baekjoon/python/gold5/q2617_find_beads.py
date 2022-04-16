# https://www.acmicpc.net/problem/2617
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().rstrip().split())
heavy_board = [[] for _ in range(N+1)]
light_board = [[] for _ in range(N+1)]
for _ in range(M):
    heavy, light  = map(int, input().split())
    heavy_board[light].append(heavy)
    light_board[heavy].append(light)

def find(graph, start, cnt):
    visited[start] = True
    for ele in graph[start]:
        if not visited[ele]:
            cnt += 1
            cnt = find(graph, ele, cnt)
    return cnt

def find_heavy(start, cnt):
    global heavy
    if heavy[start] == -1 : heavy[start] = 0
    ret = heavy[start]
    for heavier in heavy_board[start]:
        if heavy[heavier] == -1:
           ret += find_heavy(heavier) + 1
            

    heavy[start] = ret
    return ret


def find_light(start):
    global light
    if light[start] == -1: light[start] = 0
    ret = heavy[start]


    for lighter in light_board[start]:
        if light[lighter] == -1:
            ret +=  find_light(lighter) + 1

    light[start] = ret
    return ret

ans = 0
mid = (N+1) // 2
for i in range(1, N+1):
    visited = [0] * (N+1)
    if find(heavy_board, i, 0) >= mid:
        ans += 1
        continue
    if find(light_board, i, 0) >= mid:
        ans += 1

print(ans)



