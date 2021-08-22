def solution(n):
    cnt = 1
    before = 0
    now = 1
    while cnt != n :
        temp = now 
        now = before + now 
        before = temp 
        cnt += 1 
    print(now)
    return now % 1234567

print(solution(100))
