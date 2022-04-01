def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return n
    return n * factorial(n-1)

import sys
input = sys.stdin.readline

print(factorial(int(input())))
