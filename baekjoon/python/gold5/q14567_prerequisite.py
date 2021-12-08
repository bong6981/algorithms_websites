## https://www.acmicpc.net/problem/14567
import sys
input = sys.stdin.readline

from collections import deque

def solution():
    n, m = map(int, input().split())

    board = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    time = [0] * (n+1)

    for _ in range(m) :
        a, b = map(int, input().split())
        board[a].append(b)
        indegree[b] += 1
    
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            time[i] = 1

    while q:
        now = q.popleft()
        for i in board[now]:
            indegree[i] -= 1
            time[i] = max(time[i], time[now] + 1)
            if indegree[i] == 0:
                q.append(i)
    
    for t in time[1:]:
        print(t, end=' ')


solution()


    