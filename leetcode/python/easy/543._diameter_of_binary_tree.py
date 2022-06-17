# 96 ms, 16.5 MB
# https://leetcode.com/problems/diameter-of-binary-tree/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if root == None:
            return 0
        
        
        def find(node):
            
            
            if node.left and node.right:
                left_result = find(node.left)
                right_result = find(node.right)
                left_ret = max(left_result[0]+1, right_result[0]+1)
                right_ret = max(max(left_result[1], right_result[1]), left_result[0] + right_result[0] + 2) 
                return (left_ret, right_ret)
            
            if not node.left and not node.right:
                return (0, 0)
            
            result = (0, 0)
            if node.left:
                result = find(node.left)
            if node.right:
                result = find(node.right)
            return (result[0]+1, max(result[0]+1, result[1]))
            
        
        return find(root)[1]

             

            # 왼쪽에서 최대 깊이 + 오른쪽에서 최대 깊이 
#             # 왼쪽에서 최대 경로 vs 오른쪽에서 최대 거리 
        
        
#         global tmp_cnt
#         tmp_cnt = 0
#         def find_root(node, cnt):
#             global tmp_cnt
#             tmp_cnt = cnt

#             if node.left and node.right:
#                 return node
#             if node.left:
#                 return find_root(node.left, cnt+1)
#             if node.right:
#                 return find_root(node.right, cnt+1)
#             return None

#         new_root = find_root(root, 0)
#         if not new_root:
#             return tmp_cnt
        
        
#         def max_depth(node):
#             q = collections.deque([node])
#             d = 0
            
#             while q:
#                 d += 1
#                 for _ in range(len(q)):
#                     now = q.popleft()
#                     if now.left:
#                         q.append(now.left)
#                     if now.right:
#                         q.append(now.right)
#             return d
        

#         l = max_depth(new_root.left)
#         r = max_depth(new_root.right)
#         print(tmp_cnt, l, r)

#         ans = l+r
      
#         return max(ans, max(l, r) + tmp_cnt)
    