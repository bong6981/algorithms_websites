# https://leetcode.com/problems/minimum-distance-between-bst-nodes/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        global ans, prev
        prev = -sys.maxsize
        ans = sys.maxsize
        def search(node):
            global ans, prev
            
            if node.left:
                search(node.left)
            
            ans = min(ans, node.val-prev)
            prev = node.val
            
            if node.right:
                search(node.right)
            
        search(root)
        return ans 
            
            
            
            

        
        