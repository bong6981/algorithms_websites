## https://leetcode.com/problems/combination-sum/
## 89 ms, 14.2 MB
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def search(arr, sidx):
            ing_sum = sum(arr)
            if ing_sum > target:
                return
            if ing_sum == target:
                ans.append(arr[:])
                return
            
            if sidx == len(candidates):
                return
            
            for i in range(sidx, len(candidates)):
                search(arr+[candidates[i]], i);
        
        search([], 0)
        
        return ans
                
                
            
        