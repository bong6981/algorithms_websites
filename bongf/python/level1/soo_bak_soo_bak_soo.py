def solution(n):
    answer = '수박' * (n//2)
    if ( n % 2 == 1) :
        answer += '수'
    return answer

def solution2(n):
    s = "수박" * n
    return s[:n]

print(solution(3))
print(solution2(3))