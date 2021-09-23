def solution(record):
    nickname = {}
    data = []
    
    for r in record :
        r = r.split(" ")
        if(r[0] == "Enter"):
            data.append([r[1], "님이", " 들어왔습니다."])
            nickname[r[1]] = r[2]
        elif(r[0] == "Leave"):
            data.append([r[1], "님이", " 나갔습니다."])
        else :
            nickname[r[1]] = r[2]
    
    answer = []
    for d in data :
        d[0] = nickname[d[0]]
        answer.append("".join(d))
    
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))

## printer를 써거 깔끔하게 
def solution(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer

