## https://www.acmicpc.net/problem/5618
def solution():
    n = int(input())
    numbers = list(map(int, input().split()))
    gcd_num = gcd(numbers[0], numbers[1])
    if n == 3 :
        gcd_num = gcd(gcd_num, numbers[2])
    
    answer = []
    for i in range(1, (int) (gcd_num**0.5)+1):
        if gcd_num % i  == 0:
            answer.append(i)
            d = gcd_num / i
            if d != i :
                answer.append(int(d))
    answer.sort()
    return answer


def gcd(x, y):
    x, y = max(x, y), min(x, y)
    t = 1
    while t > 0:
        t = x % y
        x, y = y, t
    return x    

answer = solution()
for a in answer:
    print(a)
    


