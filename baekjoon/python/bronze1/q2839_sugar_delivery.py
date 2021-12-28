# https://www.acmicpc.net/problem/2839
def solution():
    n = int(input())
    q, r = divmod(n, 5)
    possible = False
    while q >= 0:
        if r % 3 == 0 :
            possible = True
            break
        q -= 1
        r += 5
    if not possible :
        return -1 
    return q + r // 3

print(solution())
