## https://school.programmers.co.kr/learn/courses/30/lessons/68646
def solution(a):
    min_from_left = [0] * (len(a))
    min_from_right = [0] * (len(a))
    
    min_num = 1000000001
    for i in range(len(a)):
        if min_num > a[i]:
            min_num = a[i]
        min_from_left[i] = min_num
    
    min_num = 1000000001
    for i in range(len(a)-1, -1, -1):
        if min_num > a[i]:
            min_num = a[i]
        min_from_right[i] = min_num
    
    cnt = 0
    for i in range(len(a)):
        if min_from_left[i] == a[i] or min_from_right[i] == a[i]:
            cnt += 1
            
    return cnt
