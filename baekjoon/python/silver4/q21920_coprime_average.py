import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
x = int(input())

def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

ans = []
for a in A:
    if gcd(a, x) == 1:
        ans.append(a)
print(f"{sum(ans)/len(ans):.6f}") 


