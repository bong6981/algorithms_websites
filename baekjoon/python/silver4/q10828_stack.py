# https://www.acmicpc.net/problem/10828
import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    stack = []
    for _ in range(n):
        order = input().rstrip()
        if order.startswith('push'):
            num = int(order.split(" ")[1])
            stack.append(num)
        elif order == 'pop':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])
                stack = stack[:-1]
        elif order == 'size':
            print(len(stack))
        elif order == 'empty':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif order == 'top':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1]) 

solution()
