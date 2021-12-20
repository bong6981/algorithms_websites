## https://www.acmicpc.net/problem/14425
import sys
input = sys.stdin.readline

def solution():
    n, m = map(int, input().rstrip().split())
    
    dic = {}
    order = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for o in order:
        dic[o] = []

    for _ in range(n):
        s = input().rstrip()
        dic[s[0]].append(s)

    cnt = 0
    for _ in range(m):
        x = input().rstrip()
        if x in dic[x[0]]:
            cnt += 1
    return cnt

print(solution())
