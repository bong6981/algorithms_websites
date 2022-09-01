# https://school.programmers.co.kr/learn/courses/30/lessons/67258?language=python3
from collections import defaultdict

def solution(gems):
    left = 0
    right = 0
    info = defaultdict(int)
    gems_kind = list(set(gems))
    gems_cnt = len(gems_kind)
    
    answer=[]
    cnt = 100005
    
    while left <= (len(gems) - gems_cnt) and right <= len(gems):     
        kind = len(info)
        if kind == gems_cnt:
            if (right - left + 1) < cnt:
                answer = [left+1, right]
                cnt = right - left + 1
            info[gems[left]] -= 1
            if info[gems[left]] == 0:
                del info[gems[left]]
            left += 1 
            continue
        
        if right == len(gems):
            break
        
        info[gems[right]] += 1
        right += 1 
    
    return answer
