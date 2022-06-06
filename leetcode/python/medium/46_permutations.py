## 56 ms, 14.1 MB
# https://leetcode.com/problems/permutations/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        ans = []
        visited = [False] * l
        
        def search(i, arr):
            if i == l:
                new_arr = []
                for e in arr:
                    new_arr.append(e)
                ans.append(new_arr)
                return
            
            for j in range(l):
                if not visited[j]:
                    visited[j] = True
                    arr.append(nums[j])
                    search(i+1, arr)
                    arr.pop()
                    visited[j] = False
        
        search(0, [])
        return ans
            
        