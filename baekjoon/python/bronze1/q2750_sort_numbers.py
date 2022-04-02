import sys

input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for _ in range(n)]
for n in sorted(numbers):
    print(n)
