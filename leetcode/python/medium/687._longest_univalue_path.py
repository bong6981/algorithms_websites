# 	477 ms, 	18 MB
#   https://leetcode.com/problems/longest-univalue-path/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            ans = 0
            if node == None:
                return
            
            if not node.left and not node.right:
                return 0
            
            retl = 0
            retr = 0
            if node.left  :
                if node.left.val == node.val:
                    retl = dfs(node.left) + 1
                    ans = max(ans, retl)
                    self.answer = max(self.answer, retl)
                else:
                    ret = dfs(node.left)
                    self.answer = max(self.answer, ret)
            
            if node.right :
                if node.right.val == node.val:
                    retr = dfs(node.right) + 1
                    ans = max(ans, retr)
                    self.answer = max(self.answer, retr)
                else:
                    ret = dfs(node.right)
                    self.answer = max(self.answer, ret)
            
            if retl and retr :
                self.answer = max(self.answer, retl+retr)
            
            return ans 
                
        dfs(root)
        return self.answer
                
        