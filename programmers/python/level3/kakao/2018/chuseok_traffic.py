## https://programmers.co.kr/learn/courses/30/lessons/17676?language=python3

## 다른풀이 : 더 느림 
def solution2(lines):
    global stack
    answer = 0
    sort_by_end = []
    for line in lines:
        date, time, lead_time = line.split(" ")
        e_h, e_m, e_s = time.split(":")
        e_h = int(e_h)
        e_m = e_h * 60 + int(e_m)
        e_s, e_ss = map(int, e_s.split("."))
        e_s = e_m * 60 + e_s
        e_ss = e_s * 1000 + e_ss

        lead_time = lead_time[:-1].split(".")
        lead_time_s = int(lead_time[0])
        if len(lead_time) == 1:
            lead_time_ss = "000"
        else:
            lead_time_ss = lead_time[1]
        if len(lead_time_ss) == 1:
            lead_time_ss = "00" + lead_time_ss
        if len(lead_time_ss) == 2:
            lead_time_ss = "0" + lead_time_ss
        lead_time_ss = lead_time_s * 1000 + int(lead_time_ss)

        start_tme = e_ss - lead_time_ss + 1
        sort_by_end.append((start_tme, e_ss + 999))
    
    answer = 0
    print(sort_by_end)
    for i, line in enumerate(sort_by_end):
        cnt = 0
        e_t = line[1]
        for j in range(i, len(sort_by_end)):
            if e_t >= sort_by_end[j][0]:
                cnt+=1
        answer = max(answer, cnt)
    return answer


import datetime
## 시간계산 더 간단하게 
def solution_time(lines):
    global stack
    answer = 0
    sort_by_start = []
    for line in lines:
        date, time, lead_time = line.split(" ")

        lead_time = datetime.timedelta(seconds=float(lead_time[:-1]))
        e_t = datetime.datetime.strptime(date+" "+time, "%Y-%m-%d %H:%M:%S.%f")
        start_tme = e_t - lead_time + datetime.timedelta(seconds=0.001)
        sort_by_start.append((start_tme, e_t + datetime.timedelta(seconds=0.999)))
    
    sort_by_start.sort()
    stack = []
    answer = 0
    for line in sort_by_start:
        stack.append((line[1], line[0]))
        stack.sort()
        s_t = line[0]
        while len(stack) > 1 :
            t_t = stack[0][0]
            if t_t < s_t :
                stack.pop(0)
                continue
            break
        if answer < len(stack) :
            answer = len(stack)
        print(stack)
    return answer

def solution(lines):
    global stack
    answer = 0
    sort_by_start = []
    for line in lines:
        date, time, lead_time = line.split(" ")
        e_h, e_m, e_s = time.split(":")
        e_h = int(e_h)
        e_m = e_h * 60 + int(e_m)
        e_s, e_ss = map(int, e_s.split("."))
        e_s = e_m * 60 + e_s
        e_ss = e_s * 1000 + e_ss

        lead_time = lead_time[:-1].split(".")
        lead_time_s = int(lead_time[0])
        if len(lead_time) == 1:
            lead_time_ss = "000"
        else:
            lead_time_ss = lead_time[1]
        if len(lead_time_ss) == 1:
            lead_time_ss = "00" + lead_time_ss
        if len(lead_time_ss) == 2:
            lead_time_ss = "0" + lead_time_ss
        lead_time_ss = lead_time_s * 1000 + int(lead_time_ss)

        start_tme = e_ss - lead_time_ss + 1
        sort_by_start.append((start_tme, e_ss + 999))
    
    print(sort_by_start)
    sort_by_start.sort()
    print(sort_by_start)
    stack = []
    answer = 0
    for line in sort_by_start:
        stack.append((line[1], line[0]))
        stack.sort()
        s_t = line[0]
        while len(stack) > 1 :
            t_t = stack[0][0]
            if t_t < s_t :
                stack.pop(0)
                continue
            break
        if answer < len(stack) :
            answer = len(stack)
        print(stack)
    return answer

# print(solution([
# "2016-09-15 01:00:04.001 2.0s",
# "2016-09-15 01:00:07.000 2s"
# ]))

# print(solution([
# "2016-09-15 01:00:04.002 2.0s",
# "2016-09-15 01:00:07.000 2s"
# ]))

# print(solution([
# "2016-09-15 20:59:57.421 0.351s",
# "2016-09-15 20:59:58.233 1.181s",
# "2016-09-15 20:59:58.299 0.8s",
# "2016-09-15 20:59:58.688 1.041s",
# "2016-09-15 20:59:59.591 1.412s",
# "2016-09-15 21:00:00.464 1.466s",
# "2016-09-15 21:00:00.741 1.581s",
# "2016-09-15 21:00:00.748 2.31s",
# "2016-09-15 21:00:00.966 0.381s",
# "2016-09-15 21:00:02.066 2.62s"
# ]))

# print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))
# print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))
print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))
