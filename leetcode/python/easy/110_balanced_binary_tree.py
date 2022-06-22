# 	60 ms,	19 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def search(node):
            if not node:
                return (0, True)
            
            if not node.left and not node.right:
                return (1, True)
            
            left = 0
            right = 0 
            
            if node.left:
                left, ret = search(node.left)
                if ret == False:
                    return (-1, False)
            
            if node.right :
                right, ret = search(node.right)
                if ret == False:
                     return (-1, False)
                
            print("abs(left-righ) : ", abs(left-right))
            if abs(left-right) > 1:
                return (-1, False)
            
            return (max(left, right)+1, True)
    
        return search(root)[1]
            
            