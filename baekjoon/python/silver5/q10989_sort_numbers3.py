import sys
input = sys.stdin.readline

arr = [0] * 10001 
n = int(input())
for _ in range(n):
    num = int(input())
    arr[num] += 1

for i in range(10001):
    if arr[i] > 0:
        for _ in range(arr[i]):
            sys.stdout.write(str(i) + '\n')
