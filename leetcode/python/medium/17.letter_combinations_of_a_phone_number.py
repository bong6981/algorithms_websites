# 54 ms, 13.9 MB
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        strs = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        
        answer = [] 
        def search(i, arr):
            if i == len(digits):
                answer.append("".join(arr))
                return
            else:
                num = digits[i]
                str_ = strs[int(num)]
                for j in range(len(str_)):
                    arr.append(str_[j])
                    search(i+1, arr)
                    arr.pop()
        
        search(0, [])
        return answer
                    

        