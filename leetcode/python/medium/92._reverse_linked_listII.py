# https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
## 41ms, 15mb
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #find start 
        cnt = 0
        now = ListNode()
        now.next = head
        head = now
        
        while cnt < left-1:
            now = now.next
            cnt += 1
        start_prev = now 
        start = now.next
        now = start
        cnt += 1
        start_prev.next = None
        
        #find last
        while cnt < right:
            now = now.next
            cnt += 1
        last_next = now.next
        now.next = None
        last = now
        print(start.val, last.val)
        
        ##sort
        now = start
        tmp2 = now
        while True:
            if now == last:
                break
            tmp1 = now.next
            now.next = last.next
            last.next = now
            now = tmp1
        
        print(now)
        start_prev.next = now
        print(head)
        tmp2.next = last_next
        
        return head.next
            
            
            
        
