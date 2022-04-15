from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

def sol():
    for i in range(1, V+1):
        if color[i] == 0:
            color[i] = 1
            q = deque()
            q.append(i)
            while q:
                now = q.popleft()
                for e in graph[now]:
                    if color[e] == color[now]:
                        print("NO")
                        return
                    if color[e] == 0:
                        color[e] = -color[now]
                        q.append(e)
    print("YES")

for _ in range(t):
    V, E = map(int, input().rstrip().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        x, y = map(int, input().rstrip().split())
        graph[x].append(y)
        graph[y].append(x)
    
    color = [0] * (V+1)
    possible = True
    sol()
 





            
