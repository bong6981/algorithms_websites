# 8:42 
# 2086ms, 18.7MB
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        distinct_nums = set(nums)
        answer = {}
        for n in distinct_nums :
            c = nums.count(n)
            answer[n] = c
        answer = [k for k, v in sorted(answer.items(), key=lambda item:-item[1])]
        return answer[:k]
        