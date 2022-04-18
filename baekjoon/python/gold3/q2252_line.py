# https://www.acmicpc.net/problem/2252
from collections import deque
from genericpath import samefile
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
board = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
    small, tall = map(int, input().rstrip().split())
    board[small].append(tall)
    indegree[tall] += 1

result = []
q = deque()

for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)
while q:
    now = q.popleft()
    result.append(now)

    for des in board[now]:
        indegree[des] -= 1
        if indegree[des] == 0:
            q.append(des)

print(*result)



