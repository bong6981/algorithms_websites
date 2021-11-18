def solution(dartResult):
    score = []
    area = ['S', 'D', 'T']
    for i in range(len(dartResult)) :
        x = dartResult[i]
        if x.isdecimal() :
            if i != 0 and x == '0' and dartResult[i-1] == '1' :
                score[-1] = 10
            else : 
                score.append(int(x))
        elif x in area:
            score[-1] **= (area.index(x)+1)
        elif x == '*' :
            score[-1] *= 2
            if len(score) != 1 :
                score[-2] *= 2
        else :
            score[-1] *= -1
    return sum(score)


## 숫자를 담는 n을 따로 둬서 10을 더할 수 있도록 
def solution_before(dartResult):
    score = []
    n = ''
    for i in dartResult:
        if i.isnumeric():
            n += i 
        elif i == 'S':
            score.append(int(n) ** 1)
            n = ''
        elif i == 'D':
            score.append(int(n) ** 2)
            n = ''
        elif i == 'T':
            score.append(int(n) ** 3)
            n = ''
        elif i == '*':
            score[-1] *= 2     
            if len(score) > 1:
                score[-2] *= 2
        else:
            score[-1] *= -1 
    return sum(score)

## 10는 replace로 하고, score의 마지막 index를 변수로 두는 방식  
def solution2(dartResult):
    score = []
    area = ['S', 'D', 'T']
    dartResult = dartResult.replace('10', 'k')

    i = -1
    for j in dartResult:
        if j in area :
            score[i] **= (area.index(j)+1)
        elif j == '*':
            score[i] *= 2
            if i != 0 :
                score[i - 1] *= 2
        elif j == '#':
            score[i] *= (-1)
        else:
            if(j == 'k') :
                j = '10'
            score.append(int(j))
            i += 1
    return sum(score)


print(solution2("1S2D*3T"))
print(solution2("1D2S#10S"))
# print(solution("1D2S0T"))
# print(solution("1S*2T*3S"))
# print(solution("1D#2S*3S"))
# print(solution("1T2D3D#"))
# print(solution("1D2S3T*"))