def solution(price, money, count):
    p = sum(price * i for i in range(1,count+1))
    return p - money if p > money else 0

print(solution(3, 20, 4))
