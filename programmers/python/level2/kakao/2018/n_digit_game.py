
## https://programmers.co.kr/learn/courses/30/lessons/17687

numbers = '0123456789ABCDEF'
def solution(n, t, m, p):
    answer = '0'
    num = 0
    while len(answer) <= (t -1) * m  + p :
        answer = answer + convert(num, n) 
        num += 1
    return answer[p-1::m][:t]
    
def convert(num, n):
    converted = ''
    while num:
        num, mod = divmod(num, n)
        converted = numbers[mod] + converted
    return converted

    

def solution_fail(n, t, m, p):
    from collections import deque
    total = (t-1) * (m) + p
    print(total)
    tube = deque([i * m + p for i in range(t)])
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    print(tube)

    ## 각 자리 수당 몇 개의 수가 있냐( * digit 한 수까지만 해)  
    sum = n
    n_digit_count = [n]
    digit = 2
    while sum < total :
        temp = (n-1) * (n ** (digit-1)) 
        sum += temp * digit
        n_digit_count.append(temp)
        digit += 1
    
    print(n_digit_count)
    
    answer = ''
    while tube:
        now = tube.popleft()
        print("now", now)
        digit = 0
        sum_count = 0
        for i, count in enumerate(n_digit_count):
            sum_count = (count * (i+1)) ## digtit 자리수의 총 글자수 
            if now <= sum_count :
                digit = i + 1
                break
            else:
                now -= sum_count
        print(digit)
        bunzae, zari = divmod(now, digit)
        print(bunzae, zari)

        if(digit == 1):
            answer += numbers[bunzae-1] 
            print(answer)
            continue

        if zari != 0 :
            bunzae += 1
        
        bunzae_number = []
        stored_digit = digit
      
        while(len(bunzae_number) < stored_digit): 
            mok, rest = divmod(bunzae, n**(digit-1))
            print("mok, rest", mok, ",", rest)
            if rest == 0:
                bunzae_number.append(numbers[mok])
                while(len(bunzae_number) != stored_digit):
                    bunzae_number.append(numbers[n-1])
                break
            if bunzae_number == []:
                bunzae_number.append(numbers[mok+1])
            else:
                bunzae_number.append(numbers[mok])
            if mok == 0:
                bunzae_number.append(numbers[rest-1])
            bunzae = rest
            digit -= 1
        if(zari == 0):
            answer += bunzae_number[-1]
        else:
            answer += bunzae_number[zari-1]
        print(bunzae_number)
        print(answer)
    return answer

print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 2))
print(solution(16,16,2,1))
# print(solution(16, 4, 5, 2))
