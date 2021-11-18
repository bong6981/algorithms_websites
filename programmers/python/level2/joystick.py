def solution(name):
    aidx = [] 
    
    answer = 0
    for i in range(len(name)):
        if(name[i] != 'A') :
            answer += min(ord(name[i]) - ord('A'), 91-ord(name[i]))
            aidx.append(i)
    
    lastidx = len(name)-1 
    def getlength(p, to) :
        if(p <= to):
            return min(to - p, p + 1 + lastidx - to)
        else :
            return min(p-to, lastidx - p + 1 + to)
    
    p = 0
    if p in aidx :
        aidx.remove(p)

    while len(aidx) > 0 :
        length1 = getlength(p, aidx[0])
        length2 = getlength(p, aidx[-1])
        if(length1 <= length2):
            answer += length1
            p = aidx[0]
            
        else :
            answer += length2
            p = aidx[-1]         
        aidx.remove(p)
        
    return answer

# print(solution("JEROEN"))
# print(solution("JAN"))
print(solution("AAA"))
# print(solution("BBBBAABBB"))
# print(solution("ZAAAZZZZZZZ"))







