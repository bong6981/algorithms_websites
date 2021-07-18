# 시간초과 (remove는 시간 효율성이 낮다. 매번 하나하나 뒤져가며 찾아야 하기 때문)
# def solution(participant, completion):
#     for x in completion :
#         participant.remove(x)
#     answer = participant[0]
#     return answer

def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion.append("")
    for x, y in zip(completion, participant) :
        if( x != y ):
            return y 

def solution_2(participant, completion) :
    from collections import Counter
    answer = Counter(participant) - Counter(completion)
    print(answer) #딕셔너리의 값으로 Counter({'leo' : 1}) 출력
    return list(answer.keys())[0] #리스트로 안묶어주면 출력 안된다 

def solution_3(participant, completion) :
    from collections import Counter 
    answer = list((Counter(participant) - Counter(completion)).elements())
    return answer[0]

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(solution_3(participant, completion))