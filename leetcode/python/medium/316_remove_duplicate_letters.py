#76ms, 13.8 mb, 책풀이
#https://leetcode.com/problems/remove-duplicate-letters/
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        counter = collections.Counter(s)
        data_set = set()
        
        for c in s:
            counter[c] -= 1
            if c in data_set:
                continue
            
            while stack and stack[-1] > c and counter[stack[-1]] > 0 :
                data_set.remove(stack.pop())
            
            stack.append(c)
            data_set.add(c)
        
        return "".join(stack)
            
        