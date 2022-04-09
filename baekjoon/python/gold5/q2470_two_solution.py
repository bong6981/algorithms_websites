## https://www.acmicpc.net/problem/2470
import sys
input = sys.stdin.readline
n = int(input())
all = sorted(map(int, input().split()))

def sol():
    max_v = 2000000000
    ans = (-1, -1)
    i = 0 
    j = n - 1
    while i < j:
        mix = all[i] + all[j]
        if mix == 0:
            return (i, j)
        if abs(mix) < max_v:
            max_v = abs(mix)
            ans = (i, j) 
        if mix < 0:
            i += 1
        else:
            j -= 1
    return ans

ans = sol()
print(all[ans[0]], all[ans[1]])
