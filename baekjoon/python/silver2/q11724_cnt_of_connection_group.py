## https://www.acmicpc.net/problem/11724

def sol1():
    from collections import deque
    import sys

    input = sys.stdin.readline

    N, M = map(int, input().split())
    visited = [0 for _ in range(N+1)]
    graph = [[]for _ in range(N+1)]

    for _ in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    cnt = 0
    for i in range(1, N+1):
        queue = deque()
        if not visited[i]:
            cnt += 1
            queue.append(i)
            visited[i] = 1
            while queue:
                now = queue.popleft()
                for p in graph[now]:
                    if not visited[p]:
                        queue.append(p)
                        visited[p] = 1
    print(cnt)


def sol2():
    from collections import deque
    import sys

    input = sys.stdin.readline

    N, M = map(int, input().split())
    parent = list(range(N+1))

    def find_p(x):
        if parent[x] != x:
            parent[x] = find_p(parent[x])
        return parent[x]

    def union(x, y):
        x = find_p(x)
        y = find_p(y)
        if x < y:
            parent[y] = x
        else:
            parent[x] = y

        for _ in range(M):
            x, y = map(int, input().split())
            union(x, y)

        for i in range(1, N+1):
            find_p(i)

        print(len(set(parent[1:])))
