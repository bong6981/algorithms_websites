def solution(arr1, arr2):
    r = len(arr1)
    c = len(arr1[0])
    answer = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer
    
def solution_old(arr1, arr2):
    answer = []
    r = len(arr1)
    c = len(arr1[0])
    for i in range(r):
        temp = []
        for j in range(c):
           b = arr1[i][j] + arr2[i][j]
           temp.append(b)
        answer.append(temp)
    return answer

def solution2(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer

def solution3(A,B):
    for i in range(len(A)) :
        for j in range(len(A[0])):
            A[i][j] += B[i][j] 
    return A

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]
arr3 = [[1],[2]]
arr4 = [[3],[4]]
print(solution(arr1, arr2))
print(solution(arr3, arr4))
