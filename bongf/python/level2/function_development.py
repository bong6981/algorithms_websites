import math 

def solution(progresses, speeds):
    days = []
    for p, s in zip(progresses, speeds) :
        days.append((100-p) // s + 1 if ((100 - p) % s) != 0 else (100-p) // s)
    
    answer = [0]
    criteria = days[0]
    for d in days :
        if criteria >= d:
            answer[-1] += 1
        else :
            criteria = d
            answer.append(1)       
            
    return answer

## 작업에 필요할 날과 그것을 정답 배열과 비교해 주는 것을 한 번에 
def solution2(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]

print(solution([93, 30, 55], [1, 30, 5]))
