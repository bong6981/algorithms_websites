# https://www.acmicpc.net/problem/1260
import sys
from collections import deque

input = sys.stdin.readline

def dfs_search(board, idx, to_print, visited):
    for item in board[idx] :
        if visited[item] != 1 :
            to_print.append(item)
            visited[item] = 1
            dfs_search(board, item, to_print, visited)
    return to_print    

def bfs_search(start, board, visited):
    q = deque()
    q.append(start)
    answer = []

    while q:
        now = q.popleft()
        answer.append(now)
        for item in board[now] :
            if not visited[item] :
                q.append(item) 
                visited[item] = 1

    return answer 

def solution():
    n, m, v = map(int, input().split())
    board = [[] * (n+1) for _ in range(n+1)]
    for _ in range(m):
        x, y = map(int, input().split())
        board[x].append(y)
        board[y].append(x)
    
    for i in range(1, n+1):
        board[i].sort()
    visited = [0] * (n+1)
    visited[v] = 1
    print(" ".join(map(str, dfs_search(board, v, [v], visited))))
    visited = [0] * (n+1)
    visited[v] = 1
    print(" ".join(map(str, bfs_search(v, board, visited))))

solution()
