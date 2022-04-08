import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def pow(a, exponent):
    if exponent == 1:
        return a % c
    
    half = pow(a, exponent//2)
    
    if exponent % 2 == 1:
        return ((half * half) % c) * a % c

    return half * half % c 

print(pow(a, b))

