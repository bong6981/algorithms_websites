def solution(strings, n):
    temp = []
    if(n == 0) : 
        return sorted(strings)

    for s in strings :
        if len(s)-1 == n :
            temp.append(s[n] + s[0:n])
        else : 
            temp.append(s[n] + s[0:n] + s[n+1:len(s)])

    temp = sorted(temp)
    answer = []

    for s in temp :
        if len(s)-1 == n :
            answer.append(s[1:n+1]+ s[0])
        else : 
            answer.append(s[1:n+1] + s[0] + s[n+1:len(s)])

    return answer


## 파이썬 sort에는 key라는 옵션이 있다. 
def solution2(strings, n):
    return sorted(strings, key = lambda x : x[n])
    
def solution3(strings, n):
    def sortkey(x):
        return x[n]
    strings.sort(key=sortkey)
    return strings

strings = ["abce", "abcd", "cdx"]
n = 2
print(solution3(strings, n))
