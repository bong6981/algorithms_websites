import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

## https://www.acmicpc.net/problem/15681
def solution():
    n, r, query = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    
    parent = [0] * (n+1)
    parent[r] = r

    q = deque()
    q.append(r)

    while q :
        now = q.popleft()
        for child in graph[now] :
            if child != parent[now] :
                parent[child] = now
                q.append(child)
    
    subtree = [0] * (n+1)
    subtree[r] = n

    def count_child(root):
        cnt = 1
        if subtree[root] != 0 :
            return subtree[root]
        for child in graph[root]:
            if child != parent[root]:
                cnt += count_child(child)
        subtree[root] = cnt        
        return cnt

    for _ in range(query):
        x = int(input())
        print(count_child(x))

solution()

## https://jainn.tistory.com/m/74
def solution_other() :
    def countPoint(x):
        count[x]=1
        for i in tree[x]:
            if not count[i]:
                countPoint(i)
                count[x] += count[i]

    n, r, q = map(int, input().split())
    tree = [[] for _ in range(n+1)]
    count = [0]*(n+1)

    for i in range(n-1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    countPoint(r)

    for i in range(q):
        u = int(input())
        print(count[u])

solution_other()
