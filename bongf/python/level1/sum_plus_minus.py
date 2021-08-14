def solution(absolutes, signs):
    answer = 0
    for x in range(len(absolutes)) :
        if(signs[x] == True) :
            answer += absolutes[x]
        else :                                          
            answer -= absolutes[x]         
    return answer

absolutes = [1,2,3]	
signs = [False,False,True]
print(solution(absolutes, signs))
