## https://school.programmers.co.kr/learn/courses/30/lessons/43164?language=python3
from collections import defaultdict, deque


def solution(tickets):
    tickets.sort()
    info = defaultdict(deque)
    
    for i, t in enumerate(tickets):
        s = t[0]
        e = t[1]
        info[s].append(i)
    
    visited = [0] * len(tickets)
    def dfs(arr):
        if len(arr) == len(tickets) + 1:
            return arr
        
        start = arr[-1]
        for i in info[start]:
            if not visited[i]:
                des = tickets[i][1]
                visited[i] = True
                ret = dfs(arr+[des])
                
                if ret != []:
                    return ret
                visited[i] = False
        return []
    
    return dfs(["ICN"])
    


    
    

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
