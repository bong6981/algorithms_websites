# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val <= list2.val:
            ans = list1
            list1 = list1.next
        else:
            ans = list2
            list2 = list2.next

        now = ans
        while list1 and list2:
            if list1.val <= list2.val:
                now.next = ListNode()
                now.next.val = list1.val
                list1 = list1.next
            else:
                now.next = ListNode()
                now.next.val = list2.val
                list2 = list2.next
            now = now.next
        
        if list1:
            while list1:
                now.next = ListNode() 
                now.next.val = list1.val
                list1 = list1.next
                now = now.next
        
        if list2:
            while list2:
                now.next = ListNode()
                now.next.val = list2.val
                list2 = list2.next
                now = now.next
        return ans 
        