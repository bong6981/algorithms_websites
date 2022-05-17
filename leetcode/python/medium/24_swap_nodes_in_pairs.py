# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# https://leetcode.com/problems/swap-nodes-in-pairs/submissions/
# 65ms, 13.9MB
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        now = head
        prev = None
        start = None
        if not now:
            return now 
        
        if not now.next :
            return head
        
        start = now.next
        
        while now and now.next:
            tmp = now.next.next
            if prev:
                prev.next = now.next
            now.next.next = now
            now.next = tmp
        
            prev = now
      
            now = now.next
        return start
        
            
            