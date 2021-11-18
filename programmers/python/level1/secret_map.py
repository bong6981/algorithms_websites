def solution(n, arr1, arr2):
    answer = []
    for i in range(n) :
        s = bin(arr1[i] | arr2[i])[2:]
        s = s.replace('1', '#').replace('0', ' ')
        s = ' ' * ( n - len(s)) + s
        answer.append(s)
    return answer


def solution_before(n, arr1, arr2):
    ans = []
    for i in range(n):
        bin_str = bin(arr1[i] | arr2[i])[2:]
        ans.append(("0" *(n - len(bin_str)) + bin_str).replace("1", "#")
                                                      .replace("0", " "))
    return ans

def solution2(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        ## rjust(길이, 공백체울문자) 오른쪽 정렬
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

# n = 5
# arr1 = [9, 20, 28, 18, 11]
# arr2 = [30, 1, 21, 17, 28]

n = 6 
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]
print(solution(n, arr1, arr2))
