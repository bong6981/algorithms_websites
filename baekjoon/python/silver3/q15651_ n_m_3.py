## https://www.acmicpc.net/problem/15651
# from itertools import product

# n, m = map(int, input().split())

# data = list(range(1, n+1))
# ans = product(data, repeat=m)
# for a in ans:
#     for b in a :
#         print(b, end=" ")
#     print()



import sys
input = sys.stdin.readline

def sol():
    def rec(k):
        if k == m:
            for e in selected:
                print(e, end=" ")
            print()
            return
        
        for cand in range(1, n+1):
            selected[k] = cand
            rec(k+1)

    n, m = map(int, input().split())
    selected = [0 for _ in range(m)]
    rec(0)

sol()





