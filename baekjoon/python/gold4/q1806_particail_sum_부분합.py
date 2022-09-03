## https://www.acmicpc.net/problem/1806
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))


left = 0
right = -1
s = 0
ans = 100001
cnt = 0

for left in range(N):
    while right + 1 < N and s < S:
        right += 1
        s += arr[right]

    if s >= S:
        ans = min(ans, right-left+1)
    
    s -= arr[left]

if ans == 100001:
    print(0)
else:
    print(ans)

# 10 10 
# 1 1 1 1 1 1 1 1 1 1
