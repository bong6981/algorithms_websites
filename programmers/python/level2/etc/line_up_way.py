# def solution(n, k):
#     answer = []
#     acc = []

#     a = 1
#     for i in range(1, n+1):
#         a *= i
#         acc.append(a) # 팩토리얼 리스트 만들기 

#     print(acc)
#     num = list(i for i in range(1, n+1))

#     i = 0
#     for i in range(n, 0, -1):
#         m, k = divmod(k, acc[i-2])
#         if k == 0:
#             to_add = num[m-1]
#             answer.append(to_add)
#             num = num[:m-1] + num[m:]
#             num.sort(reverse=True)
#             answer += num
#             break
        
#         to_add = num[m]
#         answer.append(to_add)
#         num = num[:m] + num[m+1:]

#     return answer


# print(solution(3, 5))

from collections import deque

def solution(n, k):
    acc = deque([])

    a = 1
    for i in range(1, n+1):
        a *= i
        acc.appendleft(a)
    
    acc = list(acc)
    print(acc)
    num = list(i for i in range(1, n+1))
    answer = []

    for i in range(0, n):
        # answer[i]
        m, k = divmod(k, acc[i+1])

        if k == 0:
            to_add = num[m-1]
            answer.append(to_add)
            # num.remove(to_add)
            num = num[:m-1] + num[m:]
            num.reverse()
            answer += num
            break
        
        to_add = num[m]
        answer.append(to_add)
        num = num[:m] + num[m+1:]

    return answer



print(solution(3, 5))
