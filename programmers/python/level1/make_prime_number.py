def solution(nums):
    answer = 0
    for x in range(len(nums) - 2):
        first = nums[x]
        for y in range(x+1, len(nums) - 1):
            second = nums[y]
            for z in range(y+1, len(nums)):
                third = nums[z]
                sum = first + second + third
                if is_prime(sum) : 
                    answer += 1
    return answer

def is_prime(number):
    half = int(number / 2)
    for i in range(2,half+1):
        if (number % i) == 0 :
            return False
    return True

def solution_2(number):
    from itertools import combinations as cb
    answer = 0
    for x in cb(number, 3) :
        sum_num = sum(x)
        if is_prime(sum_num):
            answer += 1
    return answer

def solution_3_is_prime(number):
    answer = 0
    for i in range(2, int(number**0.5)+1):
        if number % i == 0 :
            return 0
    return 1
    

def solution_3(number):
    from itertools import combinations as cb
    return sum( solution_3_is_prime(sum(x)) for x in cb(number, 3))

nums = [1,2,7,6,4]
print(solution_3(nums))