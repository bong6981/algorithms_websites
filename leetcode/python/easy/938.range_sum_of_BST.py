# https://leetcode.com/problems/range-sum-of-bst/
# 308 ms, 23.1 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        global ans
        ans = 0
        
        def find(node):
            global ans
            if not node:
                return
            if  low <= node.val <= high:
                ans += node.val
            find(node.left)
            find(node.right)
        
        find(root)
        return ans
