# https://leetcode.com/problems/palindrome-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        now = head
        s = str(now.val)
        while now.next:
            now = now.next
            s += str(now.val)
        return s == s[::-1]


## 1199ms, 47mb
