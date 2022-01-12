1
from collections import deque
def solution():
    n = int(input())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    
    for i in range(n):
        for des in find(i, board, n):
            board[i][des] = 1
    
    for r in board:
        for c in r :
            print(c, end=" ")
        print()

def find(i, board, n):
    des = set()
    visited = [False for _ in range(n)]
    q = deque([i])

    while q:
        now = q.popleft()
        visited[now] = True
        for to, possible in enumerate(board[now]):
            if possible :
                des.add(to)
                if not visited[to]:
                    des.add(to)
                    q.append(to)
    return des

solution()
# 10:26 소요시간 22분 

