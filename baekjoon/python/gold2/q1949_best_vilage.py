#10:23
import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline
sys.setrecursionlimit(100005)

N = int(input())
people = [0] + list(map(int, input().rstrip().split()))
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    A, B = map(int, input().rstrip().split())
    graph[A].append(B)
    graph[B].append(A)


def dfs(now, prev):
    dp[now][1] += people[now]
    for des in graph[now]:
        if des == prev: continue
        dfs(des, now)
        dp[now][0] += max(dp[des])
        dp[now][1] += dp[des][0]



dp = [[0, 0] for _ in range(N+1)]
dfs(1, 0)
print(max(dp[1]))


