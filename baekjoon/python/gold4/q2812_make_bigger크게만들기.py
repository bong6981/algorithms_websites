## https://www.acmicpc.net/problem/2812
import sys
input = sys.stdin.readline

n, to_erase = map(int, input().split())
to_filled = n - to_erase
numbers = list(map(int, list(input().rstrip())))

ans = []
for search_idx in range(n):
    while to_erase > 0 and len(ans) != 0 and ans[-1] < numbers[search_idx]:
        ans.pop()
        to_erase -= 1
    ans.append(numbers[search_idx])

if to_erase > 0:
    ans = ans[:-to_erase]

print("".join(str(ele) for ele in ans))



    

