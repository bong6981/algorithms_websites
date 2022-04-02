## https://www.acmicpc.net/problem/10971

import sys 
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

ans = INF
def travel(visited, last, start, cnt, cost):
    global ans

    if cost > ans:
        return

    if cnt == n:
        cost_to_start_point = graph[last][start]
        if  cost_to_start_point != 0:
                ans = min(ans, cost + cost_to_start_point)
        return

    for i, v in enumerate(graph[last]) :
        if v != 0 and not visited[i]:
            visited[i] = True
            travel(visited, i, start, cnt+1, cost + v)
            visited[i] = False

for i in range(n):
    visited = [False for _ in range(n)]
    visited[i] = True
    travel(visited, i, i, 1, 0)

print(ans)


