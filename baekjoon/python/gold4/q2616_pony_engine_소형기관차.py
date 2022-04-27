## https://www.acmicpc.net/problem/2616
import sys
input = sys.stdin.readline

N = int(input().rstrip())
people = [0] + list(map(int, input().rstrip().split())) 

acc = [0] * (N+1)
s = 0
for i, p in enumerate(people):
    s += p
    acc[i] = s

max_len = int(input().rstrip())

dp = [[0] * (N+1) for _ in range(4)]
for i in range(1, 4):
    for j in range(i * max_len, N+1):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-max_len] + acc[j] - acc[j-max_len])

print(dp[3][N])

