def solution(n, m):
    answer = []
    x = min(n, m)
    y = max(n, m)
    gcd = 1
    temp = []
    for i in range(1, int(x**0.5) + 1) :
        if x % i == 0 :
            temp.append(i)
            temp.append(x//i)
    for i in temp : 
        if y % i == 0 :
            gcd = max(i, gcd)

    answer.append(gcd)
    answer.append((n // gcd) * (m // gcd) * gcd)
    return answer

# 유클리드 호제법 사용 
def solution2(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer

def solution3(n,m):
    gcd = lambda a,b : b if not a%b else gcd(b, a%b)
    lcm = lambda a,b : a*b//gcd(a,b)
    return [gcd(n, m), lcm(n, m)]

print(solution(3,12))
print(solution(2,5))
print(solution(9,6))


