#56 ms, 16.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        global ans
        ans = 0
        
        def search(node, lev):
            global ans
            ans = max(ans, lev)
            if node.left:
                search(node.left, lev+1)
            if node.right:
                search(node.right, lev+1)
        
        if root == None:
            return 0
        search(root, 1)
        return ans
                