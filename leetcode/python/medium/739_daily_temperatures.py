# https://leetcode.com/problems/daily-temperatures/
# 2039ms, 25.6 MB
import heapq
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tmp = []
        answer = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            heapq.heappush(tmp, (t, i))
            while tmp and tmp[0][0] < t:
                v, idx = heapq.heappop(tmp)
                answer[idx] = i - idx
        
        return answer
            
      