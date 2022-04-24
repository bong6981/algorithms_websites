# https://www.acmicpc.net/problem/14501
import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input().rstrip())

requests = []
for _ in range(N):
    s, e  = map(int, input().split())
    requests.append((s, e))

requests.sort(reverse=True)

last_s = 2 ** 31
cnt = 0
for s, e in requests:
    if e <= last_s:
        cnt += 1
        last_s = s

print(cnt)


    


