# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
## https://leetcode.com/problems/reverse-linked-list/submissions/
## 45ms, 15.5MB
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        now = head
        if (not now) or (not now.next):
            return now 
        while now:
            arr.append(now)
            tmp = now.next 
            now.next = None
            now = tmp   
        
        ans = arr[-1]
        now = ans
        for i in range(len(arr)-2, -1, -1):
            now.next = arr[i]
            now = now.next
        
        return ans 
