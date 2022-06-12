# https://programmers.co.kr/learn/courses/30/lessons/17678
from collections import deque

# def solution(n, t, m, timetable):
#     ## start 
#     st = 60 * 9 
#     ## last_car 
#     lt = st + t * (n-1)
    
#     crew = []
#     for time in timetable:
#         h, minute = map(int, time.split(":"))
#         time = h * 60 + minute
#         if time <= lt:
#             crew.append(time)
    
#     crew.sort()
#     crew = deque(crew)
    
    
#     ans = 0
#     for i in range(1, n+1):
#         if i == n:
#             print(crew, len(crew), m)
#             if len(crew) < m:
#                 ans = lt
#             else:
#                 early_then = crew[m-1]
#                 ans = early_then - 1
        
#         time = st + (i - 1) * t
#         cnt = m 
#         while crew and crew[0] <= time and cnt > 0:
#             crew.popleft()
#             cnt -= 1
    
#     h = str(ans // 60)
#     m = str(ans % 60)
#     ans = ''
#     if len(h) == 1:
#         ans += '0'
#     ans += h
#     ans += ':'
#     if len(m) == 1:
#         ans += '0'
#     ans += m
#     return ans


def solution(n, t, m, timetable):
    ## start 
    st = 60 * 9 
    ## last_car 
    lt = st + t * (n-1)
    
    crew = []
    for time in timetable:
        h, minute = map(int, time.split(":"))
        time = h * 60 + minute
        if time <= lt:
            crew.append(time)
    
    crew.sort()
    print(crew)

    ans = 0
    crew_idx = 0
    for i in range(1, n+1):
        if i == n:
            print(crew, crew_idx, (crew_idx + (m - crew_idx)-1), m)
            if len(crew) - crew_idx  < m:
                ans = lt
            else:
                early_then = crew[crew_idx + m-1]
                ans = early_then - 1
            break
        
        time = st + (i - 1) * t
        cnt = m 
        while crew_idx < len(crew) and crew[crew_idx] <= time and cnt > 0:
            crew_idx += 1
            cnt -= 1
    
    h = str(ans // 60)
    m = str(ans % 60)
    ans = ''
    if len(h) == 1:
        ans += '0'
    ans += h
    ans += ':'
    if len(m) == 1:
        ans += '0'
    ans += m
    return ans

            
# print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, 	["09:10", "09:09", "08:00"]))
        
        
