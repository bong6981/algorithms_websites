def solution(x):
    return True if (x % sum( int(i) for i in iter(str(x)))) == 0 else False

# string을 for문 돌리면 ch가 나와서 iter 필요 없고 
# 저번에 했던 것과 같이 if else 써줄 필요 없다. 

def solution2(n):
    return n % sum([int(c) for c in str(n)]) == 0

print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))

