import math

def solution(left, right):
    l = int(math.sqrt(left))
    if l != math.sqrt(left) :
        l += 1
    
    r = int(math.sqrt(right))   
    s = sum( x for x in range(left,right+1))    
    return s - (sum( x ** 2 for x in range(l, r+1)))*2

## 루트는 x**0.5해줄 수 있다. 
def solution_2(left, right):
    answer = 0
    for i in range(left, right+1):
        if i**0.5 == int(i**0.5) :
            answer -= i
        else :
            answer += i 
    return answer
    
print(solution(24,27))