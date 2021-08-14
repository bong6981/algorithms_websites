## 이중포문을 돌면 시간초과 
def solution(N, stages):
    rate = {}
    for i in range(1, N+1):
        d = 0
        n = 0
        for j in range(len(stages)):
            if stages[j] >= i :
                d += 1
                if stages[j] == i:
                    n += 1
        if d==0 :
            rate[i] = 0
        else :   
            rate[i] = n / d
    
    return sorted(rate, key = lambda x: rate[x], reverse = True)

def solution_old(N, stages):
    fail_dic = {}
    d = len(stages)
    for stage in range(1, N+1):
        if d !=0:
            count = stages.count(stage)
            fail_dic[stage] = count/d
            d -= count
        else:
            fail_dic[stage] = 0 
    return sorted(fail_dic, reverse=True, key=lambda x: fail_dic[x])
