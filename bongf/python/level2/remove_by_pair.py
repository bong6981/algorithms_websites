def solution(s):
    answer = []
    ref = ''
    for c in s :
        if(c==ref):
            ## 여기 pop() 을 안쓰고 answer = answer[:-1] 로 하면 효율성 에러 
            answer.pop()
            if(len(answer)>0):
                ref = answer[-1]
            else :
                ref = ''
        else: 
            answer.append(c)
            ref = c
    print(answer)
    if(len(answer)==0):
        return 1 
    return 0

## 정확성 통과 bt 시간 초과 
def solution_fail(s):
    idx = 0; 
    while idx < len(s)-1 : 
        print(s, idx)
        if s[idx] == s[idx+1]:
            s = s[0:idx] + s[idx+2:] 
            idx -= 1 
            if(idx<0):
                idx = 0 
        else : 
            idx += 1 

    if(len(s)==0):
        return 1
    return 0 


print(solution("baabaa"))

