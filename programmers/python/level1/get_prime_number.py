## 처음에 똑같은 방식으로 하는데 배열에 1과 0대신 해당 숫자를 쓰니 remove 등을 써야 해서 효율성 에러 
def solution(n):
    temp = [0] * (n + 1)
    temp[2] = 1 
    for i in range(3, n+1, 2):
        temp[i] = 1
    
    for x in range(3, int(n**0.5)+1, 2) :
        for y in range(x, n//x + 1, 2) :
            temp[x*y] = 0
    
    return temp.count(1)


def solution2(n):
    temp = [True] * (n+1)
    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if temp[i] == True:           # i가 소수인 경우
            for j in range(i+i, n+1, i): # i이후 i의 배수들을 False 판정
                temp[j] = False
    return temp.count(True) - 2

def solution3(n) :
    temp = set(range(2,n+1))
    m = int(n ** 0.5)
    for i in range(2, m+1) :
        if i in temp :
            temp -= set(range(2*i, n+1, i))
    return len(temp)

print(solution2(10))
