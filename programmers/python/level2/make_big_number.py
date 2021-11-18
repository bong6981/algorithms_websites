## max 대신 idx를 활용하자 
## number를 변환하지 말고 인덱스를 사용하자 
## 검사하는 숫자가 9일 때 더이상 검사 종료 -> 이 조건이 있어야 테케 10번 통과 
def solution(number, k):
    l = len(number) - k 
    answer = []
    cur = 0 
    while(l!=0) :
        if number[cur] != '9' :
            for i in range(cur+1, len(number)-l+1) :
                if(number[i]> number[cur]):
                    cur = i
                    if(number[cur] == '9') :
                        break
        answer.append(number[cur])
        cur += 1
        l -= 1
    return "".join(answer)
   
## 10번 fail 
## 문자열 더하기가 오래 걸리나? answer = '', answer += 방식에서 배열로 바꿨지만 fail
def solution_try3(number, k):
    l = len(number) - k 
    answer = []
    while(l!=0) :
        # 여기 주석 해도 10번 fail 안해도 8번 통과 
        # if(l==len(number)) :
        #     answer.append(number)
        #     break
        # if(k==1) :
        #     temp = []
        #     for i in range(len(number)) :
        #         temp.append(number[:i] + number[i+1:])
        #     return sorted(temp, reverse = True)[0]             
        # else :
            # print(number, number[:len(number)-l+1], k, l)
            temp = max(number[:len(number)-l+1])
            answer.append(str(temp))
            idx = number.index(temp)
            number = number[idx+1:]
            l -= 1
    return "".join(answer)


from itertools import combinations as cb
## 시간초과 4/12만 통과 
## 가능한 idx를 combination을 써서 구한다음 그 모든 경우의 수들 중 가장 큰 수 
def solution_try2(number, k):
    number = list(number)
    answer = []
    l = len(number) - k
    for idx in cb(list(range(len(number))), l) :
        temp = []
        for i in idx :
            temp.append(number[i])
        answer.append(int("".join(temp)))
    return str(sorted(answer, reverse=True)[0])




## 시간초과 4/12만 통과 
## 뽑아야 하는 수의 갯수(l)로 가능한 조합을 다 계산한다음 제일 큰 수 뽑는 방식 
def solution_try(number, k):
    answer = []
    l = len(number) - k
    
    def get_number(left, fix, total, idx) :
        if(idx <= len(left)) :
            if(len(fix) == total):
                answer.append(int("".join(fix)))
            else :
                for i in range(idx, len(left)) :
                    originleft = left[:]
                    originfix = fix[:] 
                    x = left[i]
                    left.remove(x)
                    fix.append(x)
                    get_number(left, fix, total, i)
                    left = originleft
                    fix = originfix

    fix = []
    get_number(list(number), fix, l, 0)
    return str(sorted(answer, reverse=True)[0])


#####
# 위의 풀이랑 다른 점은 나 : while (l (len(number) -k)) 안에 for문 
# 여기 풀이는 for문으로 number의 len만큼 한 번만 돌면서 중간에 while을 걸어줌. 그 whild의 조건에 k 변수가 들어가고 
# 결국 여기선 for문은 한 번만 돌게 되고, k로 뒤에 최소 몇개가 있는지 확인  
def solution2(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)

#sol2를 조금 더 정리한 부분, (첫 요소 넣는 부분이나, 마지막에 k처리)
def solution2(number, k):
    st = []
    for i in range(len(number)):
        while st and k > 0 and st[-1] < number[i]:
            st.pop()
            k -= 1
        st.append(number[i])
    return ''.join(st[:len(st) - k])




print(solution2("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
print(solution("987654321", 1))

