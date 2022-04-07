import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    num = int(input())

    while len(stack) > 0 and stack[-1] <= num :
        stack.pop()
    stack.append(num)

print(len(stack))
