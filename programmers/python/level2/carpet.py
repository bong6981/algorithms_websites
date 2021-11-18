def solution(brown, yellow):
    divisor = []
    answer = []
    t = brown + yellow
    for i in range(1, int(t**0.5)+1):
        if(t%i == 0) :
            divisor.append((i, t//i))
    for x,y in divisor :
        if( 2*(x+y) - 4) == brown : 
            answer = [x,y]

    return sorted(answer, reverse=True)

# 작은 네모의 약수를 구하고, 테두리는 그 작은네모 *2 + 4 = brown임을 이용한다.
# 작은수부터 확인해서 나누므로 solution1에서 sort해줄 필요가 없다. 
# 근의공식으로 푼 것은 java에 
def solution2(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]


# print(solution(10,2))
print(solution2(8,1))
# print(solution(24,24))

