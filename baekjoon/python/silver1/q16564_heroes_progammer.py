## https://www.acmicpc.net/problem/16564

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
levels = [int(input()) for _ in range(n)]
levels.sort()
min_v = levels[0]
start = 0

def sol():
    global k, min_v, start
    ans = 0
    while True:
        last_min_idx = find(min_v, start, n-1, levels)
        cnt = last_min_idx + 1
        
        if cnt == n:
            ans = min_v + (k//cnt)
            break

        to_add = k // cnt 
        gap = levels[last_min_idx+1] - levels[last_min_idx]

        if to_add <= gap:
            ans = min_v + to_add
            break
        
        min_v += gap
        k -= gap * cnt
        start = last_min_idx + 1
    print(ans)


def find(target, start, end, levels):
    ans = start
    while start <= end:
        mid = (start + end) // 2
        if levels[mid] == target:
            ans = mid
            start = mid + 1
        elif levels[mid] > target:
            end = mid -1

    return ans

sol()
