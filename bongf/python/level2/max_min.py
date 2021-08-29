def solution(s):
    arr = list(map(int, s.split(" ")))
    arr.sort()
    return str(arr[0]) + " " + str(arr[len(arr)-1])


## min과 max를 활용하자 
def solution2(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))

print(solution("-1 0 -2"))
print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))
