def solution(s):
    low = s.lower()
    return True if low.count('p') == low.count('y') else False 
    ## 그냥 true false 없애도 된다 return low.count('p') == low.count('y')

print(solution('Pyy'))