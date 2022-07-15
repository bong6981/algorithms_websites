N = int(input())
K = int(input())

start = 1
end = N ** 2
ans = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(1, N+1):
        cnt += min(mid // 2, N)

    if cnt >= K:
        ans = mid
        end = mid - 1
    else:
        start += 1

print(ans)

