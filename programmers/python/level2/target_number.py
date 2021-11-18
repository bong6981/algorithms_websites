

def solution(numbers, target):
    cnt = 0
    sl = []

    def search(index, sum, sign, cnt):
        sum += (numbers[index]) * sign
        if index == len(numbers)-1 : 
            if(sum == target) :
                return 1
            return 0
        else : 
            x = search(index+1, sum, 1, cnt)
            y = search(index+1, sum, -1, cnt)
            cnt += x
            cnt += y
        return cnt

    cnt += search(0,0,1,0)
    cnt += search(0,0,-1,0)
    return cnt


def solution_edit_1(numbers, target):
    def search(index, sum, sign):
        sum += (numbers[index]) * sign
        if index == len(numbers)-1 : 
            if(sum == target) :
                return 1
            return 0
        else : 
            return search(index+1, sum, 1) + search(index+1, sum, -1)
    
    cnt = search(0,0,1) + search(0,0,-1)
    return cnt

def solution2(numbers, target) :
    if not numbers :
        if target == 0:
            return 1
        return 0
    else :
        return solution2(numbers[1:], target-numbers[0]) + solution2(numbers[1:], target+numbers[0])


# print(solution([1], 1))    
# print(solution([1,2], 3))   
# print(solution([1,2,3], 6))
print(solution([1, 1, 1, 1, 1], 3))
