## https://leetcode.com/problems/implement-queue-using-stacks/submissions/
## 14MB, 41ms
class MyQueue:

    def __init__(self):
        self.st = []
        self.tmp = []
        

    def push(self, x: int) -> None:
        if len(self.st) == 0:
            self.st.append(x)
        else:
            for _ in range(len(self.st)):
                self.tmp.append(self.st.pop())
            
            self.st.append(x)
            for _ in range(len(self.tmp)):
                self.st.append(self.tmp.pop())

    def pop(self) -> int:
        return self.st.pop()
        

    def peek(self) -> int:
        return self.st[-1]

    def empty(self) -> bool:
        return len(self.st) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
