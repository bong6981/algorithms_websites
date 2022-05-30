# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# https://leetcode.com/problems/merge-k-sorted-lists/
# 5169ms, 17.5MB
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans_head = ListNode()
        ans = ans_head
        
        tmp = []
        for i in range(len(lists)):
            if lists[i]:
                tmp.append(lists[i])
        
        lists = tmp
                
        
        if len(lists) == 1 and lists[0] == None:
            return lists[0]
        while True:
            if not len(lists):
                break
            lists.sort(key=lambda x: x.val)
            ans.next = lists[0]
            if not lists[0].next:
                lists.pop(0)
            else:
                lists[0] = lists[0].next
            ans.next.next = None
            ans = ans.next
        return ans_head.next
            
                    
                
        