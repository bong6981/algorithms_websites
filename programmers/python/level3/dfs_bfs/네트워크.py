## https://school.programmers.co.kr/learn/courses/30/lessons/43162?language=python3
from collections import deque 
def solution(n, computers):
    
    candidates = [1] * n
    cnt = 0
    while 1 in candidates:
        now = candidates.index(1)
        cnt +=1 
        q = deque()
        q.append(now)
        
        while q:
            cur = q.popleft()
            candidates[cur] = 0
            for i in range(n):
                if computers[cur][i] == 1 and candidates[i] == 1:
                    q.append(i)
    return cnt
            
        
