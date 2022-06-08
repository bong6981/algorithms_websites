## 642 ms, 15.9 MB
# https://leetcode.com/problems/combinations/
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def search(start, depth, arr):
            if depth == k:
                ele = []
                for e in arr:
                    ele.append(e)
                ans.append(ele)
                return
            
            for e in range(start, n+1):
                search(e+1, depth+1, arr+[e])
            
        search(1, 0, [])
        return ans
        