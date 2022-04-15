import sys


input = sys.stdin.readline

V, E = map(int, input().rstrip().split())
edges = []
for _ in range(E):
    A, B, C = map(int, input().rstrip().split())
    edges.append((C, A, B))

edges.sort()
parents = [i for i in range(V+1)]

def find_p(x):
    if parents[x] != x:
        parents[x] = find_p(parents[x])
    return parents[x]

def union(x, y):
    x = find_p(x)
    y = find_p(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

ans = 0
for c, x, y in edges:
    if find_p(x) != find_p(y):
        union(x, y)
        ans += c

print(ans)



