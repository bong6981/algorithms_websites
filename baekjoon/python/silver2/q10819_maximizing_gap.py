import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

ans = 0

def cal(arr):
    ans = 0
    for i in range(0, n-1):
        ans += abs(arr[i]-arr[i+1])
    return ans

def perm(visited, arr):
    global ans
    if len(arr) == n:
        ans = max(ans, cal(arr))
        return

    for i in range(n):
        if not visited[i] :
            visited[i] = True
            arr.append(numbers[i])
            perm(visited, arr)
            arr.pop()
            visited[i] = False

perm([False for _ in range(n)], [])
print(ans)

from itertools import permutations
for p in permutations(numbers):
    ans = max(ans, cal(list(p)))
print(ans)
