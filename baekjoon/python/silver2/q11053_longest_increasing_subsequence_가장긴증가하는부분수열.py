# https://www.acmicpc.net/problem/11053

import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input().rstrip())
dp = [1] * N
numbers = list(map(int, input().rstrip().split()))

max_len = 1
for i in range(1, len(numbers)):
    num = numbers[i]
    for j in range(i-1, -1, -1):
        if numbers[j] < num:
            dp[i] = max(dp[i], dp[j]+1) 
            max_len = max(max_len, dp[i])

print(max_len)

