def solution(nums):
    max = int( len(nums) / 2 )
    kind = len(set(nums))
    if kind >= max :
        return max
    else : 
        return kind

def solution_2(nums):
    return min(len(nums)/2, len(set(nums)))

nums = [3,3,3,2,2,2,2,2,2]
print(solution(nums))