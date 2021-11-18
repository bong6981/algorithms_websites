def solution(arr1, arr2): 
    ## (l x m ) * (m x n) = (l x n)
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]

    for i in range(len(arr1)) :
        for j in range(len(arr2[0])) :
            answer[i][j] = 0
            for k in range(len(arr2)) :
                answer[i][j] += arr1[i][k] * arr2[k][j]

    return answer

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))

def solution2(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

B = [[1,2,3], [4,5,6]]
for a, b in zip(*B):
    print(a, b)

## numpy 사용 불가인 코테도 있다고 함
import numpy as np
def productMatrix(A, B):
    return (np.matrix(A)*np.matrix(B)).tolist()

