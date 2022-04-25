## https://www.acmicpc.net/problem/2098
import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

INF = int(1e9)
N = int(input().rstrip())
graph = []
cache = [[INF] * (1<<N) for _ in range(N)]

for _ in range(N):
    graph.append(list(map(int, input().rstrip().split())))

def dp(start, visited):
    if cache[start][visited] != INF:
        return cache[start][visited]
    
    if visited == (1 << N) - 1:
        if graph[start][0]:
            return graph[start][0]
        return INF
    
    for there in range(1, N):
        if not graph[start][there]:
            continue
        if visited & (1 << there):
            continue
        next_visited = visited | (1 << there)
        cache[start][visited] = min(cache[start][visited], dp(there, next_visited) + graph[start][there])
   
    return cache[start][visited]


print(dp(0, 1))

