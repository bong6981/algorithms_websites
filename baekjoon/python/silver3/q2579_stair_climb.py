import sys
input = sys.stdin.readline

N = int(input())
stairs = [0] * (N+1)
for i in range(1, N+1):
    stairs[i] = int(input().rstrip())

dp = [[0, 0] for _ in range(N+1)]

dp[1][0] = stairs[1]


for i in range(2, N+1):
    dp[i][0] = max(dp[i-2]) + stairs[i]
    dp[i][1] = dp[i-1][0] + stairs[i]

print(max(dp[N]))

## 전칸이랑 전전칸만 하면 공간복잡도 줄일 수 있다 
