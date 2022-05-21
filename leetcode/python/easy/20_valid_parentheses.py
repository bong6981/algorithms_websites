## https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')', '{':'}', '[': ']'}
        if len(s) == 0:
            return True
        
        if len(s) == 1:
            return False
        
        stack = []
        s = collections.deque(list(s))
        while s:
            c1 = s.popleft()
            if c1 in dic:
                stack.append(c1)
            else:
                if not stack:
                    return False
                c2 = stack.pop()
                if c2 in dic and dic[c2] == c1:
                    continue
                return False
        if stack:
            return False
        return True
        