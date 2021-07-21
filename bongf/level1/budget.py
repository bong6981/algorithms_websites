def solution(d, budget):
    d = sorted(d)
    answer = 0
    for num in d :
        if budget < num :
            break
        budget = budget - num
        answer += 1     
    return answer

d = [2,2,3,3]
budget = 10
print(solution(d, budget))