def solution(n):
    answer = 0
    for x in range(2, n):
        if (n-1) % x == 0:
            answer = x
            break
    return answer

def solution(n):
    return next(i for i in range(2, n) if n % i == 1)
