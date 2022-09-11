## https://school.programmers.co.kr/learn/courses/30/lessons/64062
'''
이분탐색을 이용한 풀이 solution1 
'''

def check(m, stones, k):
    
    cnt = 0
    for stone in stones:
        if stone < m:
            cnt += 1
        else:
            cnt = 0
        if cnt == k:
            return False
    return True 
    

def solution1(stones, k):
    m = max(200000000, len(stones))
    start = 1
    end = m
    answer = 1
    while(start <= end):
        mid = (start + end) // 2
        if check(mid, stones, k):
            start = mid + 1
            answer = max(answer, mid)
        else:
            end = mid - 1
    return answer

'''
슬라이딩 윈도우 - heapq를 이용한 풀이 - solution2
'''
import heapq

def solution2(stones, k):
    heap = []
    answer = 200000000
    for i, stone in enumerate(stones):
        heapq.heappush(heap, (-stone, i))
        if i < (k-1):
            continue
        
        while heap and heap[0][1] <= (i-k):
            heapq.heappop(heap)
        
        answer = min(-heap[0][0], answer)
    
    return answer


'''
슬라이딩 윈도우 -  deque를 이용한 풀이 - solution3
'''
from collections import deque
def solution3(stones, k):
    
    q = deque()
    answer = 200000000
    for i, stone in enumerate(stones):
        if q and q[0] == (i - k):
            q.popleft()
        
        while q:
            if stones[q[-1]] < stone:
                q.pop()
            else:
                break
        
        q.append(i)
        if i >= k - 1:
            answer = min(answer, stones[q[0]])
        
    return answer

