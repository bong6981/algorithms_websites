from itertools import permutations as pm
def solution(numbers):
    arr = list(numbers)
    answer = []
    for i in range(1, len(numbers)+1):
        arr2 = list(pm(numbers, i))
        for ch in arr2 :
            if ch[0] == '0' :
                continue
            x = int("".join(ch))
            if x == 1 :
                continue
            if (is_prime(x)) :
                answer.append(x)
    answer = set(answer)
    return len(answer)

def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1) :
        if(num % i == 0 ) :
            return False
    return True

## is_prime 쓴 것이 좀 더 빨랐다. 
def solution2(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, pm(list(n), i + 1)))) # 비트 or 연산후 할당 |= 
    a -= set(range(0, 2)) # {0, 1} 을 제거 
    print(a)
    for i in range(2, int(max(a) ** 0.5) + 1):
        print(set(range(i * 2, max(a) + 1, i)))
        a -= set(range(i * 2, max(a) + 1, i)) #약간 체 거르는 것 처럼 그 배수들을 싹다제거
    return len(a)

print(solution2("011"))


##0520 풀이
# def is_prime(num):
#     if num == 0 or num == 1 :
#         return False
#     for i in range(2, int(num**0.5)+1):
#         if num % i == 0:
#             return False
#     return True
    
# def search(digit, numbers, depth, checked):
#     if depth == digit:
#         num = int("".join(numbers[:depth]))
#         if num in checked:
#             return 0
            
#         checked.add(num)
#         if is_prime(num):
#             return 1
#         return 0
    
#     cnt = 0
#     for i in range(depth, len(numbers)):
#         numbers[depth], numbers[i] = numbers[i], numbers[depth]
#         cnt += search(digit, numbers, depth+1, checked)
#         numbers[depth], numbers[i] = numbers[i], numbers[depth]

#     return cnt 
        
# def solution(numbers):
#     answer = 0
#     checked = set()
#     for i in range(1, len(numbers)+1):
#         answer += search(i, list(numbers), 0, checked)
#     return answer


# # print(solution("17"))
# print(solution("011"))
