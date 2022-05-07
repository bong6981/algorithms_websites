
## https://leetcode.com/problems/3sum/
def threeSum(nums):
    nums.sort()

    tmp_ret = set()
    for i, n in enumerate(nums):
        left = i+1
        right = len(nums)-1
        while left < right:
            x = nums[left] + nums[right]
            if -n < x:
                right -= 1
            elif -n > x:
                left += 1
            else:
                tmp_ret.add((n, nums[left], nums[right]))
                right -= 1
    ret = []
    for e in tmp_ret:
        ret.append([e[0], e[1], e[2]])
    return ret

print((threeSum([-1,0,1,2,-1,-4])))    
print((threeSum([])))    
print((threeSum([0])))    
print((threeSum([1,1,-2])))    
print((threeSum([-4,-2,-1])))    
            
        