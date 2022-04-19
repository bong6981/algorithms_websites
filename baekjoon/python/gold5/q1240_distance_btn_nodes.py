# https://www.acmicpc.net/problem/1240
def sol_lca():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**9)

    N, M = map(int, input().split())

    graph = [[] for _ in range(N+1)]
    parent = [(0,0)] * (N+1)
    d = [0] * (N+1)
    visited = [False] * (N+1)

    for _ in range(N-1):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    def dfs(x, depth):
        visited[x] = True
        d[x] = depth
        for des, c in graph[x]: 
            if visited[des]:
                continue
            parent[des] = (x, c)
            dfs(des, depth+1)

    dfs(1, 0)
    def lca(x, y):
        x_cost = 0
        y_cost = 0
        while d[x] != d[y]:
            if d[x] > d[y]:
                p, c = parent[x]
                x = p
                x_cost += c
            else:
                p, c = parent[y]
                y = p
                y_cost += c
        
        while x != y:
            x, c = parent[x]
            x_cost += c
            y, c = parent[y]
            y_cost += c
        
        return x_cost + y_cost


    for _ in range(M):
        x, y = map(int, input().split())
        print(lca(x, y))


def sol():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**9)

    N, M = map(int, input().split())

    graph = [[] for _ in range(N+1)]

    for _ in range(N-1):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))


    def search(x, y, cost):
        global visited
        visited[x] = 1
        if x == y:
            print(cost)
            return

        for des, c in graph[x]:
            if not visited[des]:
                search(des, y, cost+c)


    for _ in range(M):
        x, y = map(int, input().split())
        visited = [0] * (N+1)
        search(x, y, 0)
