#45ms, 14.1MB
## https://leetcode.com/problems/subsets/
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        for i in range(1<<n):
            tmp = []
            for j in range(n):
                if(i & (1 << j)):
                    tmp.append(nums[j])
            ans.append(tmp)
        
        return ans

            