from collections import deque
def solution():
    n = int(input())
    board = [[] for _ in range(n+1)]
    for _ in range(n-1):
        x, y = map(int, input().split())
        board[x].append(y)
        board[y].append(x)

    q = deque()
    parent = [0] * (n+1)
    for i in board[1]:
        parent[i] = 1
        q.append(i)
    while q:
        now = q.pop()
        for i in board[now]:
            if parent[now] != i :
                parent[i] = now
                q.append(i)
    for k in range(2, n+1):
        print(parent[k])

solution()
