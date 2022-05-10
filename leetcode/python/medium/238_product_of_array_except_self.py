#10:09
#228ms, 21.1MB
def productExceptSelf(nums) :
    ans = [1] * len(nums)

    s = 1
    for i, n in enumerate(nums):
        ans[i] *= s
        s *= n 

    s = 1
    for i in range(len(nums)-1, -1, -1):
        ans[i] *= s
        s *= nums[i]
    
    return ans
