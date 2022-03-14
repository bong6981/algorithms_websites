## https://www.acmicpc.net/problem/15652
n, m = map(int, input().split())

data = list(range(1, n+1))
ans = []


def sol(k):
    if len(ans) == m :
        for a in ans:
            print(a, end=" ")
        print()
    else:
        for i in range(k, n+1):
            ans.append(i)
            sol(i)
            ans.pop()

sol(1)

