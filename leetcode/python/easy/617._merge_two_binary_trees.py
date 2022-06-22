# https://leetcode.com/problems/merge-two-binary-trees/
# 139 ms, 15.5 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        #왼쪽 그래프에 오른쪽 그래프 더하는 방식 
        def merge(node1, node2):
            node1.val += node2.val
            if node2.left: 
                tmp = node2.left
                node2.left = None
                if node1.left:
                    merge(node1.left, tmp)
                else:
                    node1.left = tmp
            if node2.right:
                tmp = node2.right
                node2.right = None
                if node1.right:
                    merge(node1.right, tmp)
                else:
                    node1.right = tmp
            
        if root1 and root2:
            merge(root1, root2)
            return root1
        
        if root1:
            return root1
        if root2:
            return root2
        return root1
            
        