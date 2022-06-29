import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().rstrip().split()))
cnt = 0

# 버블 sort 개념 복습. 당연 시간 초과 N제곱의 시간 복잡도 
# for i in range(N-1, -1, -1):
#     swap = False
#     for j in range(i):
#         if(nums[j] > nums[j+1]):
#             nums[j], nums[j+1] = nums[j+1], nums[j]
#             swap = True
#             cnt += 1
#     if not swap:
#         break

# print(cnt)

## 병합정렬을 이용한 풀이
def merge(start, mid, end):
    global cnt, nums
    sorted = []
    i, j = start, mid+1
    while(i <= mid and j <= end):
        if nums[i] <= nums[j]:
            sorted.append(nums[i])
            i += 1
        else:
            sorted.append(nums[j])
            j += 1
            cnt += (mid - i + 1)
    if i <= mid:
        sorted = sorted + nums[i:mid+1]
    if j <= end:
        sorted = sorted + nums[j:end+1]
    
    for i in range(len(sorted)):
        nums[i+start] = sorted[i]

def mergesort(start, end):
    if start < end:
        mid = (start + end) // 2
        mergesort(start, mid)
        mergesort(mid+1, end)
        merge(start, mid, end)

mergesort(0, N-1)
print(cnt)















