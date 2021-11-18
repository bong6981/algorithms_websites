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
