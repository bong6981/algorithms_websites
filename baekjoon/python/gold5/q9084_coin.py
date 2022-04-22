## https://www.acmicpc.net/problem/9084
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    coins = list(map(int, input().rstrip().split()))
    m = int(input().rstrip())

    dp = [0] * (m+1)
    dp[0] = 1

    for coin in coins:
        for money in range(m+1):
            if money >= coin:
                dp[money] += dp[money-coin]
    
    print(dp[m])
