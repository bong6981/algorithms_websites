# https://www.acmicpc.net/problem/1922
def solution():
    global parent
    n = int(input())
    parent = [i for i in range(n+1)]
    connections = []
    m = int(input())
    for _ in range(m):
        a, b, c = map(int, input().split())
        connections.append((c, a, b))
    connections.sort()
    total = 0
    for conn in connections:
        c, a, b = conn
        if find_p(a) != find_p(b):
            union(a, b)
            total += c
    return total

def find_p(x):
    if parent[x] != x:
        parent[x] = find_p(parent[x])
    return parent[x]

def union(x, y):
    x = find_p(x)
    y = find_p(y)
    if x == y :
        return
    if x < y :
        parent[y] = x
    else:
        parent[x] = y

print(solution())
