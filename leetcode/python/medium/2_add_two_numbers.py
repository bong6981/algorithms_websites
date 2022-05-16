# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
### 119ms, 14mb
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        now = ans
        up = 0
        while l1 or l2 or up:
            v = up
            if l1:
                v += l1.val
                l1 = l1.next
            
            if l2:
                v += l2.val
                l2 = l2.next

            v, up = v % 10, v // 10 
            now.next = ListNode(v)
            now = now.next
        
        
        return ans.next
            
## TIme out
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         ans = ListNode()
#         now = ans
#         up = 0
#         while l1 and l2:
#             v = up
#             v += l1.val
#             v += l2.val
#             v, up = v % 10, v // 10 
            
#             now.next = ListNode(v)
#             now = now.next
#             l1 = l1.next
#             l2 = l2.next
        
        
#         while l1:
#             v = up
#             v += l1.val
#             if v >= 10:
#                 v, up = v % 10, v // 10 
#                 now.val = v
#                 now.next = ListNode(v)
#                 now = now.next
#             else:
#                 now.val = v
#                 now.next = l1.next
#                 break
        
#         while l2:
#             v = up
#             v += l2.val
#             if v >= 10:
#                 v, up = v % 10, v // 10 
#                 now.val = v
#                 now.next = ListNode(v)
#                 now = now.next
#             else:
#                 now.val = v
#                 now.next = l2.next
#                 break
        
#         if up != 0:
#             now.val = up
        
#         return ans.next
            
            
            
        
        