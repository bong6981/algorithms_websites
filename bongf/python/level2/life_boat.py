def solution(people, limit):
    people.sort(reverse=True)
    min = len(people) - 1
    answer = 0
    
    for i, maxw in enumerate(people) :
        if(i > min) :
            break 
        if(maxw + people[min] <= limit) :
            min -= 1
        answer += 1 
        
    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
