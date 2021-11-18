def solution(a, b):
    return sum(i for i in range(min(a, b), max(a, b)+1))
    ## 다른사람 풀이 보니까 for안써주고 sum(range(min(a,b),max(a,b)+1)) 이렇게 가능

print(solution(3,3))