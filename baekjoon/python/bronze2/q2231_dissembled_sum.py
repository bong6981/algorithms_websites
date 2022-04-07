## https://www.acmicpc.net/problem/2231
import sys
input = sys.stdin.readline

n = int(input())
min_ans = n - len(str(n)) * 9
if min_ans < 0 :
    min_ans = 1

for i in range(min_ans, n+1):
    num = sum(map(int, str(i)))
    num += i
    if num == n:
        print(i)
        break
    if i == n:
        print(0)

