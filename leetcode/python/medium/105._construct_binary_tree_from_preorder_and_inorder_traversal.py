# 174 ms, 	53.5 MB
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        global preorder_idx 
        preorder_idx = 0
        
        def make_tree(inorder):
            global preorder_idx
            
            root = TreeNode()
            root.val = preorder[preorder_idx]
            preorder_idx += 1
            new_idx = inorder.index(root.val)
            left = inorder[:new_idx]
            if left:
                root.left = make_tree(left)
            right = inorder[new_idx+1:]
            if right:
                root.right = make_tree(right)
            
            return root
        
        return make_tree(inorder)
