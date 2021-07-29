def solution(arr):
    answer = [arr[0]]
    for x in arr :
        if x != answer[len(answer)-1] :
            answer.append(x)
    return answer

arr = [4,4,4,3,3]
print(solution(arr))
