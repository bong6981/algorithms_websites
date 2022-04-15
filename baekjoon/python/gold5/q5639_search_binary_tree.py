## https://www.acmicpc.net/problem/5639
import sys
sys.setrecursionlimit(10**9) ## 10의 5승

def search(start, end):
    now = nums[start]
    if start == end:
        print(now)
        return

    idx = start + 1
    while idx <= end and nums[idx] < now:
        idx += 1
    
    ## 뒤에가 now보다 큰 애들만 있는 경우 가 아닌 경우 
    if idx != start + 1:
        search(start+1, idx-1)
      
    ## 뒤에가 now 보다 작은 애들만 있는 경우가 아닌 경우 
    if idx <= end:
        search(idx, end)
    
    print(nums[start])

input = sys.stdin.readline
nums = []
while True:
    try:
        nums.append(int(input().rstrip()))
    except:
        break

search(0, len(nums)-1)



    
 
    





