import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

N, K = map(int, input().split())
items = [(0, 0)]

for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V))

items.sort()

graph = [[0] * (K+1) for _ in range(len(items))]

## 푼 방법
for i in range(1, len(items)):
    for j in range(items[0][0], K+1):
        if j >= items[i][0] :
            graph[i][j] = max(items[i][1] + graph[i-1][j-items[i][0]], graph[i-1][j])
        else:
            graph[i][j] = graph[i-1][j]

print(graph)


