import sys
input = sys.stdin.readline
N = int(input().rstrip())


graph = [[0] * (10) for _ in range(N+1)]


graph[1] = [1] * (10)

for i in range(2, N+1):
    cnt = 0
    for j in range(10):
        cnt += graph[i-1][j]
        graph[i][j] = (cnt % 10007)

print(sum(graph[N])%10007) 


