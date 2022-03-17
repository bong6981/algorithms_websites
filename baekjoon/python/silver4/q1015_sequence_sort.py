## https://www.acmicpc.net/problem/1015
import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
sorted_numbers = sorted(numbers)

before = 0
dic = {}
for i, n in enumerate(sorted_numbers):
    if before != n :
        dic[n] = [i]
    else:
        dic[n].append(i)
    before = n

answer = []
for n in numbers:
    ans = dic[n][0]
    if len(dic[n]) > 1:
        dic[n].pop(0)
    answer.append(ans)

for a in answer:
    print(a, end=" ")
