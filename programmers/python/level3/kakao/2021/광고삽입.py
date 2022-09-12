## https://school.programmers.co.kr/learn/courses/30/lessons/72414?language=python3
def to_seconds(time):
    h,m,s = map(int, time.split(":"))
    return h*3600 + m*60+s

def to_string(time):
    time = str(time)
    if len(time) == 1:
        return "0"+time
    return time


def solution(play_time, adv_time, logs):
    play_time = to_seconds(play_time)
    adv_time = to_seconds(adv_time)
    
    times = [0] * (play_time+1)
    first_start = (play_time+1)
    last_end = 0
    for log in logs:
        start, end = log.split("-")
        start = to_seconds(start)
        end = to_seconds(end)
        times[start] += 1
        times[end] -= 1
        
        if first_start > start:
            first_start = start
        if last_end < end:
            last_end = end
        
    
    for t in range(first_start, last_end+1):
        if(t==0): continue
        times[t] = times[t] + times[t-1]
    
    ## 투 포인터 이용한 풀이 
    ans = sol_with_two_pinter(times, first_start, last_end, play_time, adv_time)
    ## 누적합 이용한 풀이 
    # ans = sol_with_prefix_sum(times, first_start, last_end, play_time, adv_time)
    
    h, left = divmod(ans, 3600)
    m, s = divmod(left, 60)
    
    return to_string(h) + ":" + to_string(m) + ":" + to_string(s)


### 투 포인터 이용한 풀이 
def sol_with_two_pinter(times, first_start, last_end, play_time, adv_time):
    start = max(0, first_start-adv_time)
    end = min(last_end+adv_time, play_time)
    
    
    s = sum(times[start:start+adv_time])
    left = start
    right = start+adv_time-1
    
    ans_cnt = s
    ans = start
    while right < end:
        s -= times[left]
        left += 1
        right += 1
        s += times[right]
        if s > ans_cnt:
            s = ans_cnt
            ans = left 

    return ans


### 누적합 이용한 풀이 
def sol_with_prefix_sum(times, first_start, last_end, play_time, adv_time):
    for t in range(first_start,  play_time +1):
        times[t] = times[t] + times[t-1]
        
    start = max(adv_time-1, first_start-adv_time)
    end = min(last_end+adv_time, play_time)
    
    ans_cnt = 0
    ans = None
    
    for end_time in range(start, end+1):
        if end_time >= adv_time:
            time = times[end_time] - times[end_time-adv_time]
        else:
            time = times[end_time]
        
        if time > ans_cnt:
            ans_cnt = time 
            ans = end_time-adv_time+1
    return ans
