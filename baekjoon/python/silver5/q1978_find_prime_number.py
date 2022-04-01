import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

def is_prime(number):
    if number == 1:
        return False
    for i in range(2, int(number ** 0.5)+1):
        if number % i == 0:
            return False
    return True

cnt = 0 
for n in numbers:
    if is_prime(n):
        cnt += 1

print(cnt)



