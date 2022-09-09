import collections
import sys, heapq

## heapq를 이용한 풀이 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        answer = []
        for i, v in enumerate(nums):
            heapq.heappush(heap, (-v, i))
            if i < k -1:
                continue
            while(heap and heap[0][1] <= (i - k)):
                heapq.heappop(heap)
            answer.append(-heap[0][0])
        return answer

## deque를 이용한 풀이 
def maxSlidingWindow(nums, k):
    q = collections.deque()
    ans = []
    for i, v in enumerate(nums):
        if q and q[0] == i - k:
            q.popleft()
        
        while q:
            if nums[q[-1]] < v:
                q.pop()
            else:
                break
        
        q.append(i)
        if i >= k - 1:
            ans.append(nums[q[0]])
    return ans

