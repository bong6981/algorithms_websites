def solution(x, n):
    return [x * i for i in range(1,n+1)]

print(solution(-4, 2))

def solution_old(x, n):
    answer = []
    add = x 
    for __ in range(n):
        answer.append(x)
        x += add
    return answer
