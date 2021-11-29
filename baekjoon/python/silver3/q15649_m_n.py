## https://www.acmicpc.net/problem/15649
def solution():
    n, m = map(int, input().split())
    answer = []
    def back_tracking(arr):
        if len(arr) == m:
            temp = []
            for i in range(m):
                temp.append(arr[i])
            answer.append(temp)
            return
        
        for i in range(1, n+1):
            if i in arr :
                continue
            arr.append(i)
            back_tracking(arr)
            arr.pop()

    back_tracking([])
    for a in answer:
        for i in range(m):
            print(a[i], end=' ')
        print()
            
solution()

## jh05013 님의 풀이
def other():
    from itertools import permutations 
    n, m = map(int, input().split())
    for p in permutations(range(1, n+1), m):
        print(*p)
