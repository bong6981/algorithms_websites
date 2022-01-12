# https://www.acmicpc.net/problem/1005
# 5/33
from collections import deque
import copy
import sys
input = sys.stdin.readline


def solution():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        t = [0]
        for i in map(int, input().split()) :
            t.append(i)
        indegree = [0] * (n+1)

        board = [[] for _ in range(n+1)]
        for _ in range(k):
            x, y = map(int, input().split())
            board[x].append(y)
            indegree[y] += 1
        
        w = int(input())
        result = copy.deepcopy(t)
        q = deque()
        for i in range(1, n+1):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            now = q.popleft()
            for i in board[now]:
                result[i] = max(result[i], result[now] + t[i])
                indegree[i] -= 1
                if indegree[i] == 0 :
                    q.append(i)

        print(result[w])


sys.setrecursionlimit(10000)
def solution_time_fail():
    global t
    global answer
    global board

    for _ in range(int(input())):
        answer = []
        n, k = map(int, input().split())
        t = [0]
        for i in map(int, input().split()) :
            t.append(i)

        board = [[] for _ in range(n+1)]
        for _ in range(k):
            x, y = map(int, input().split())
            board[y].append(x)

        w = int(input())
        dfs(w, 0)
        answer.sort(reverse=True)
        print(answer[0])

def dfs(now, time):
    global answer
    global board
    time += t[now]
    if board[now] == []:
        answer.append(time)
        return
    
    for to in board[now]:
        dfs(to, time)

def solution_memory_fail():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        t = [0]
        for i in map(int, input().split()) :
            t.append(i)

        board = [[] for _ in range(n+1)]
        for _ in range(k):
            x, y = map(int, input().split())
            board[y].append(x)

        w = int(input())
        q = deque([(w, 0)])
        answer = []
        while q:
            now, time = q.popleft()
            time += t[now]
            if len(board[now]) == 0 :
                answer.append(time)
            else:
                for to in board[now]:
                    q.append((to, time))

        answer.sort(reverse=True)
        print(answer[0])

solution()
