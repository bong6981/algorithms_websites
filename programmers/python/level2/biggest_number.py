def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer

def solution2(numbers) :
    numbers_str = [str(n) for n in numbers] ##  numbers = list(map(str, numbers))
    numbers_str.sort(key= lambda x : x*3, reverse=True)
    return str(int(''.join(numbers_str)))

import functools

## return 값이 true, false가 아니라 -1, 0, 1이어야 함 
def comparator(a,b):
    t1 = a+b
    t2 = b+a

    # x = int(t1) - int(t2)
    # if(x >0) :
    #     print(1)
    # elif(x==0) :
    #     print(0)
    # else:
    #     print(-1)
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0


def solution_try(numbers) :
    dic = {}
    for n in numbers :
        n = str(n)
        if n[0] in dic :
            dic[n[0]].append(n)
        else :
            dic[n[0]] = [n]

    answer = ''
    for i in range(9, -1, -1) :
        if(str(i) in dic) :
            arr = sorted(dic[str(i)], reverse=True)
            while(len(arr) != 0) :
                if(len(arr[0]) == 1) :
                    answer += arr[0]
                    arr.remove(arr[0])
                elif(len(arr[0]) ==2) :
                    if arr[0][1] >= str(i) :
                        answer += arr[0]
                        arr.remove(arr[0])
                    else :
                        if(str(i) in arr) :
                            answer += str(i)
                            arr.remove(str(i))
                        answer += arr[0]
                        arr.remove(arr[0])
                elif(len(arr[0]) == 3) :
                    if arr[0][1] > str(i) :
                        if(arr[0][2] <= str(i)) and arr[0][:2] in arr :
                            answer += arr[0][:2]
                            arr.remove(arr[0][:2])    
                        answer += arr[0]
                        arr.remove(arr[0])
                    elif arr[0][1] == str(i) :
                        if arr[0][2] >= str(i) :
                            answer += arr[0]
                            arr.remove(arr[0])
                        else : 
                            if(str(i) in arr) :
                                answer += str(i)
                                arr.remove(str(i))
                            if(str(i)+str(i) in arr) :
                                answer += (str(i)+str(i))
                                arr.remove((str(i)+str(i)))
                            answer += arr[0]
                            arr.remove(arr[0])
                    else : 
                        if(str(i) in arr) :
                            answer += str(i)
                            arr.remove(str(i))
                        if(arr[0][2] < str(i)) :
                            if(arr[0][:2] in arr) :
                                answer += arr[0][:2]
                                arr.remove(arr[0][:2])
                        answer += arr[0]
                        arr.remove(arr[0])

                else :
                    if(len(arr) == 1) :
                        answer += arr[0]
                        arr.remove(arr[0]) 
                    else :
                        for i in range(len(arr)-1, -1, -1) :
                            answer += arr[i]
                        arr = []
    if(answer[0] == '0') : return '0'
    return answer

print(solution([6, 600, 5, 4])) # 660054
print(solution([3, 30, 34, 5, 9])) #9534330
print(solution([3, 31, 311, 30, 2, 1])) #3313113021
print(solution([100, 1000, 1]))
print(solution([32, 320])) #32320
print(solution([0, 0])) #0
print(solution([0, 0, 70])) #7000
print(solution([12, 121])) # 12121
print(solution([67, 676])) # 67676
print(solution([67, 678])) # 67867
print(solution([21, 212])) # 21221
print(solution([64, 647])) # 64764
print(solution([0, 0, 0, 1000])) # 1000000
print(solution([6, 10, 2])) # 1000000

# print(True-False) ## 1 
# print(True-True) ## 0
# print(False-False) ## 0
# print(False-True) ## -1










