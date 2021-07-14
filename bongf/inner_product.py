def solution(a, b):
    answer = 0
    for i in range(len(a)) :
        answer += a[i] * b[i] 
    return answer

a = [-1,0,1]
b= 	[1,0,-1]

print(solution(a, b))