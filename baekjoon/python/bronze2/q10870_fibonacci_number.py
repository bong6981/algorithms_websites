# https://www.acmicpc.net/problem/10870
def solution():
    n = int(input())
    if n == 0 :
        return 0
    d = [0] * (n+1)
    d[0] = 0
    d[1] = 1    
    for i in range(2, n+1):
        d[i] = d[i-1] + d[i-2]
    return d[n]

print(solution())
