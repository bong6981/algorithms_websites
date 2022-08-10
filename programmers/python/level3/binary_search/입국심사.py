# https://school.programmers.co.kr/learn/courses/30/lessons/43238
def solution(n, times):
    times.sort()
    start = times[0]
    end = times[0] * n
    ans = -1
    
    while start <= end:
        mid = (start + end) // 2 ## mid 분까지 
        cover = 0
        for time in times:
            if time > mid:
                break
            cover += mid // time
        
        if cover >= n:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    
    
    return ans
 
