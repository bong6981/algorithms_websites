# 51 ms, 13.9 MB
# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        def sum_and_search(node, val):
            if not node:
                return 0
            
            ret = node.val
            # 자기 오른쪽 : 자기부모로부터 내려온 값만 보내기
            ret_r = sum_and_search(node.right, val)
            # 왼쪽 : 자기부모 + 자신 값 합해서 보내기 
            ret_l = sum_and_search(node.left, val+ret_r+node.val)
            node.val += val + ret_r
            return ret+ret_r+ret_l
        
        sum_and_search(root, 0)
        return root
       
          
        
        