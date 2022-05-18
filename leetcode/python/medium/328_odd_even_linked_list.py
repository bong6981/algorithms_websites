# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# https://leetcode.com/problems/odd-even-linked-list/submissions/
#57ms, 16.6MB
class Solution:
    
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        ans = head
        odd_end = head
        even_end = head.next
        
        while even_end.next and even_end.next.next:
            p1 = even_end.next
            p2 = even_end.next.next
            
            even_end.next = p2
            even_end = p2
            
            tmp = odd_end.next
            odd_end.next = p1
            p1.next = tmp
            odd_end = p1
        
        if even_end.next:
            p = even_end.next
            even_end.next = None
            
            tmp = odd_end.next
            p.next = tmp
            odd_end.next = p
            
        return ans
                
                
                
            

        
                
                    
                
                
        