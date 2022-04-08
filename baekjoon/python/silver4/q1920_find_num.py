## https://www.acmicpc.net/problem/1920
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
b = list(map(int, input().split()))

def bisearch(start, end, target):
    ans = -1
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == target:
            return mid
        if a[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return ans

start = 0
end = len(a) -1
for e in b:
    result = bisearch(start, end, e) 
    if result == -1:
        print(0)
    else:
        print(1)



