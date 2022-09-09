## https://school.programmers.co.kr/learn/courses/30/lessons/64064
def solution(user_id, banned_id):
    
    cand = [[] for _ in range(len(banned_id))]
    for k, b_id in enumerate(banned_id):
        for j, u_id in enumerate(user_id):
            if len(b_id) == len(u_id):
                possible = True
                for i, v in enumerate(b_id):
                    if v != "*" and v != u_id[i]:
                        possible = False
                        break
                if possible:
                    cand[k].append(j)
        
    
    ans = set()
    
    def sol(turn, ret):
        if turn == len(banned_id):
            ans.add(str(ret))
            return 
        
        for can in cand[turn]:
            if ret[can] == 0:
                ret[can] = 1
                sol(turn+1, ret)
                ret[can] = 0
    
    ret = [0] * len(user_id)
    sol(0, ret)        
        
    return len(ans)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))


