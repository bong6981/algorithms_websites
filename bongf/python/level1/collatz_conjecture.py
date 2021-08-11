def solution(num):
    answer = 0
    while answer != 500 and num != 1:
        if num%2 :
            num = num * 3 + 1
        else :
            num /= 2        
        answer += 1
    return answer if num == 1 else -1

# print(solution(6))
# print(solution(16))
print(solution(626331))

