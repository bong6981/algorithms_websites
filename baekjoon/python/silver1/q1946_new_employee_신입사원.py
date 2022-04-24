## https://www.acmicpc.net/problem/1946
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    N = int(input().rstrip())

    scores = []
    for num in range(1, N+1):
        p, i = map(int, input().rstrip().split())
        scores.append((p, i))

    scores.sort()

    low_i = scores[0][1]
    cnt = 0
    for p, i in scores[1:]:
        if i > low_i:
            cnt += 1
        elif i < low_i:
            low_i = i
    print(N-cnt)
