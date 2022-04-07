# https://www.acmicpc.net/problem/10828
import sys
from typing import Any
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

# solution()


## 7:42
class MyStack:
    
    def __init__(self, capacity: int = 10000):
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0
        pass

    def push(self, value:Any) -> None:
        self.stk[self.ptr] = value
        self.ptr += 1

    def is_empty(self) -> int:
        if self.ptr <= 0:
            return 1
        return 0

    def pop(self) -> int:
        if self.is_empty():
            return -1
        self.ptr -= 1
        return self.stk[self.ptr]
        
    def size(self) -> int:
        return self.ptr
    
    def top(self) -> Any:
        if self.is_empty():
            return -1
        return self.stk[self.ptr-1]

import sys
input = sys.stdin.readline

def sol():
    s = MyStack()
    n = int(input())
    for _ in range(n):
        order = list(input().split())
        if order[0] == "push":
            s.push(int(order[1]))
        elif order[0] == "top":
            print(s.top())
        elif order[0] == "size":
            print(s.size())
        elif order[0] == "empty":
            print(int(s.is_empty()))
        elif order[0] == "pop":
            print(s.pop())

sol()    


    
