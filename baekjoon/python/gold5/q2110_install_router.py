## https://www.acmicpc.net/problem/2110
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
homes = [int(input()) for _ in range(n)]
homes.sort()

start = 1
end = homes[n-1] - homes[0]
ans = 0
while start <= end:
    mid = (start + end) // 2
    prev = homes[0]
    left = c - 1
    for i in range(1, n):
        if homes[i] - prev >= mid:
            left -= 1
            prev = homes[i]
        if left == 0:
            break
            
    if left == 0:
        ans = mid
        start = mid + 1
    else:
        end = mid -1
print(ans)

