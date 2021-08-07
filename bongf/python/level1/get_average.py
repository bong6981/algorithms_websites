def solution(arr):
    return sum(x for x in arr) / len(arr)

# list는 for문으로 돌릴 필요도 없다. 
def solution_2(list):
    return (sum(list) / len(list))

print(solution([1,2,3,4]))
print(solution([5,5]))
