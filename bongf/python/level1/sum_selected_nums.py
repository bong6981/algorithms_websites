def solution(numbers):
    result = []
    for i in range(len(numbers)-1) :
        for j in range(i+1, len(numbers)):
            result.append( numbers[i] + numbers[j])
    return sorted(set(result))


numbers = [5,0,2,7]
print(solution(numbers))
