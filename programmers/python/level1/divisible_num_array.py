def solution(arr, divisor):
    answer = []
    for n in arr :
        if n % divisor == 0 :
            answer.append(n)
    return [-1] if len(answer) == 0 else sorted(answer) 

# 파이썬에서 0, [], " ", False 등은 거짓 그 외에 나머지 값은 참
def solution2(arr, divisor):
    return sorted([n for n in arr if n % divisor == 0]) or [-1]

arr = [3,2,6]
divisor = 10
print(solution2(arr, divisor))