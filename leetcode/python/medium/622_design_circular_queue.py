# 14.3MB, 132ms
# https://leetcode.com/problems/design-circular-queue/
class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * (k)
        self.front = 0
        self.rear = -1
        self.size = 0
        self.max_size = k

    def enQueue(self, value: int) -> bool:
        if self.size == self.max_size:
            return False
        
        self.rear += 1
        if self.rear == self.max_size:
            self.rear = 0
        self.q[self.rear] = value
        self.size += 1
        return True        

    def deQueue(self) -> bool:

        if self.size == 0:
            return False
        
        val = self.q[self.front]
        self.front += 1
        if self.front == self.max_size:
            self.front = 0
        self.size -= 1
        return True
    
        
    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.q[self.front]
        

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.q[self.rear]
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.max_size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
