def solution(n):
    a = sorted(map(int, str(n)))
    return sum( a[i-1] * 10 ** (i-1) for i in range(1, len(a)+1))

def solution(n) :
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(s))

print(solution(118372))
