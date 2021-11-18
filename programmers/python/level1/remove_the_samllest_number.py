def solution(arr):
    arr.remove(sorted(arr, reverse=True)[-1])
    return [-1] if len(arr) <= 0 else arr

def solution2(arr):
    arr.remove(min(arr))
    return [-1] if len(arr) <= 0 else arr

print(solution([4,3,2,1]))
print(solution([10]))

