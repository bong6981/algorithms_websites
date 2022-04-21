import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
coins = []
for _ in range(n):
    coins.append(int(input().rstrip()))

cnt = 0
for c in reversed(coins):
    if k >= c : 
        cnt += k // c
        k = k % c
    if k == 0:
        break

print(cnt)
