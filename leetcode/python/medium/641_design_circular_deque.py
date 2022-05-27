## 81ms, 14.6MB
## https://leetcode.com/problems/design-circular-deque/
class MyCircularDeque:

    def __init__(self, k: int):
        self.q = [0] * k
        self.max_size = k
        self.size = 0
        self.front = 0
        self.rear = 1

    def insertFront(self, value: int) -> bool:
        if self.size == self.max_size :
            return False
        
        self.q[self.front] = value
        self.front -= 1
        if self.front == -1:
            self.front = self.max_size-1
        self.size += 1
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.size == self.max_size :
            return False
        self.size += 1
        
        self.q[self.rear] = value
        self.rear += 1
        if self.rear == self.max_size :
            self.rear = 0
        return True
        

    def deleteFront(self) -> bool:
        if not self.size:
            return False
        self.size -= 1
        
        self.front += 1
        if self.front == self.max_size :
            self.front = 0
        return True
        

    def deleteLast(self) -> bool:
        if not self.size:
            return False
        self.size -= 1
        
        self.rear -= 1
        if self.rear == -1:
            self.rear = self.max_size - 1
        return True 
        

    def getFront(self) -> int:
        if not self.size:
            return -1
        if self.front + 1 == self.max_size:
            return self.q[0]
        return self.q[self.front+1]

    def getRear(self) -> int:
        if not self.size:
            return -1
        if self.rear - 1 == -1:
            return self.q[self.max_size - 1]
        return self.q[self.rear-1]
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.max_size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
