def solution():
    s_h, s_m, s_s = map(int, input().split(":"))
    e_h, e_m, e_s = map(int, input().split(":"))
    answer = [0, 0, 0]
    
    if(e_h < s_h):
        e_h += 24

    if(e_s < s_s):
        if(e_m == 0):
            e_h -= 1
            e_m = 59
        else:
            e_m -= 1
        e_s += 60
    answer[2] = e_s - s_s
    
    if(e_m < s_m):
        e_h -= 1
        e_m += 60
    answer[1] = e_m - s_m
    answer[0] = e_h - s_h

    result = ''
    for a in answer:
        a = str(a)
        if len(a) == 1 :
            result += '0'
        result += a
        result += ':'

    if result == '00:00:00:':
        return '24:00:00'
    return result[:-1]    

print(solution())
