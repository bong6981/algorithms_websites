import sys 
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
ans = 1

def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x%y)


def isPrime(num):
    for i in range(2, int(num ** 0.5)+1) :
        if num % i == 0:
            return False
    return True 

found = False
for a in A:
    if isPrime(a):
        ans = ans * a // gcd(ans, a)
        found = True

if not found:
    print(-1)
else:
    print(ans)






