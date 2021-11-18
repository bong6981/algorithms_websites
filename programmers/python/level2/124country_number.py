def solution(n):
    nums = [1, 2, 4]
    sum = 0 
    ## 자리수 구하기 i 
    for i in range(1, 19):
        sum += 3**i
        if(sum >= n):
            break
    ## 자리수 j 
    j = i
    ## 해당 자리 수의 몇 번째 수 k 
    k = n - (sum - 3**i)
    
    ans = ['4'] * j 
    

    for i in range(j):
        m, n = divmod(k, (3**(j-1-i)))
        if n == 0 :
            m -= 1
            ans[i] = str(nums[m])
            break
        else : 
            ans[i] = str(nums[m])
            k = n 
    
    
    answer = ''.join(ans)
    return answer

def solution2(n):
    num = ['1','2','4']
    answer = ''

    while n > 0 :
        n -= 1
        answer = num[n%3] + answer 
        n //= 3
        
    return answer 


print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))
print(solution(7))
print(solution(8))
print(solution(9))
print(solution(18)) ##124


