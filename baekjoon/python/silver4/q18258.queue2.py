import sys
from typing import Any
input = sys.stdin.readline

## https://www.acmicpc.net/problem/18258

## 큐로 구현했을 때 
class FixedQueue:
    def __init__(self, capacity:int) -> None:
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * capacity
    
    def is_empty(self) -> bool:
        return self.no <= 0
    
    def push(self, x:Any) -> None:
        self.que[self.rear] = x
        self.rear += 1
        self.no += 1
    
    def pop(self) -> Any:
        if self.is_empty():
            return -1
        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x
    
    def size(self) -> int:
        return self.no

    def front(self) -> int:
        if self.is_empty:
            return -1
        return self.que[self.front]
    
    def back(self) -> int:
        if self.is_empty:
            return -1
        return self.que[self.rear-1]

def solution_impl():
    que = FixedQueue()
    n = int(input())
    for _ in range(n):
        order = list(input().split())
        if len(order) == 1:
            order = order[0]
            if order == "pop":
                print(que.pop())
            elif order == "size":
                print(que.size())
            elif order == "empty":
                if que.is_empty():
                    print(1)
                else:
                    print(0)
            elif order == "front":
                print(que.front())
            elif order == "back":
                print(que.back())
        else:
            que.push(int(order[1]))

## deque 사용했을 때 
def solution_dequeue():
    from collections import deque
    arr = deque([], maxlen=2000000)

    n = int(input())
    for _ in range(n):
        order = list(input().split())
        if len(order) == 1:
            order = order[0]
            if order == "pop":
                if len(arr) == 0:
                    print(-1)
                else:
                    print(arr.popleft())
            elif order == "size":
                print(len(arr))
            elif order == "empty":
                if len(arr) == 0:
                    print(1)
                else:
                    print(0)
            elif order == "front":
                if len(arr) == 0:
                    print(-1)
                else:
                    print(arr[0])
            elif order == "back":
                if len(arr) == 0:
                    print(-1)
                else:
                    print(arr[-1])
        else:
            arr.append(int(order[1]))
                





solution_dequeue()
