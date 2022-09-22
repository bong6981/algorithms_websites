def solution(queue1, queue2):
    arr = queue1 + queue2
    
    left = 0
    right = len(queue1)
    
    target = sum(arr) // 2
    s = sum(queue1)
    cnt = 0
    while cnt <= len(queue1) * 3:
        if s == target:
            return cnt 
        if s < target:
            s += arr[right]
            right += 1
            if right == len(arr):
                right = 0
        else:
            s -= arr[left]
            left += 1
        cnt += 1
    return -1
    return -1

# print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
# print(solution([1,1,1], [5,1,1]))
# print(solution([1,1,1,8,10,9], [1,1,1,1,1,1]))
print(solution([ 1, 1, 1, 1, 1, 1, 1, 1, 1, 10], [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
