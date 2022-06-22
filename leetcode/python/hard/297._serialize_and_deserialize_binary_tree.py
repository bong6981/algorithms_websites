# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 115ms, 20.1MB
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
from collections import deque
class Codec:

    def serialize(self, root):
        ans = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                ans.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                ans.append(None)
                          
        
        ans = str(ans)
        return ans
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = list(None if i == 'None' else int(i) for i in data[1:-1].split(", "))
        if data == [None]:
            return None
        data = deque(data)
        
        root = TreeNode(data.popleft())
        q = deque([root])
        while q:
            now = q.popleft()
            left_val = data.popleft()
            right_val = data.popleft()
            if left_val != None:
                now.left = TreeNode(left_val)
                q.append(now.left)
            if right_val != None:
                now.right = TreeNode(right_val)
                q.append(now.right)
        return root 
                

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
