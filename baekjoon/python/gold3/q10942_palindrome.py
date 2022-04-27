import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input().rstrip())
given = [0] + list(map(int, input().rstrip().split()))

dp = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    dp[i][i] = 1
    if i != N and given[i] == given[i+1]:
        dp[i][i+1] = 1


for len in range(2, N+1):
    for i in range(1, N-len+2):
        j = i + len -1
        print(i, j, len)
        if given[i] == given[j] and dp[i+1][j-1] :
            dp[i][j] = 1

M = int(input().rstrip())
for _ in range(M):
    A, B = map(int, input().rstrip().split())
    print(dp[A][B])

