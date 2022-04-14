# https://www.acmicpc.net/problem/16120
import sys
input = sys.stdin.readline

stack = []
for c in input().rstrip():
    if c == 'P' and len(stack) >= 3:
        if stack[-1] == 'A' and stack[-2] == 'P' and stack[-3] == 'P':
            for _ in range(3):
                stack.pop()

    stack.append(c)

if stack == ['P']:
    print('PPAP')
else:
    print('NP') 
