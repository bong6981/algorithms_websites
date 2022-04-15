from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
parent = list(range(N+1))

for _ in range(N-1):
    x, y = map(int, input().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)

queue = deque()
queue.append(1)

while queue:
    p = queue.popleft()
    for ch in graph[p]:
        if parent[ch] == ch:
            parent[ch] = p
            queue.append(ch)

for p in parent[2:]:
    print(p)

