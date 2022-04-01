from re import T
import sys
input = sys.stdin.readline

import math

def solution1():
    for _ in range(int(input())):
        n = int(input())
        for i in range(math.ceil(n/2), 1, -1):
            if is_prime(i) and is_prime(n-i):
                print(i, n-i)
                break


def solution2():
    for _ in range(int(input())):
        n = int(input())
        prime_numbers = get_prime_numbers(n)
        ans = 0
        for i in sorted(list(prime_numbers)):
            if i > math.ceil(n/2) :
                break
            if n-i in prime_numbers:
                ans = i
        print(ans, n-ans)

def get_prime_numbers(num):
    temp = set(range(2, num+1))
    for i in range(2, int(num**0.5)+1):
        if i in temp:
            temp -= set(range(2*i, num+1, i))
    return temp
        

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True

solution2()
