from collections import deque
# https://www.acmicpc.net/problem/11728
## 다른 사람 풀이보고 포인터 써서 푼 방법, 시간이 제일 쪼금 걸리긴 한다. 
def solution():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_p = 0
    b_p = 0 
    answer = []
    while True:
        if n <= a_p:
            answer += b[b_p:]
            break
        elif m <= b_p:
            answer += a[a_p:]
            break

        if a[a_p] < b[b_p]:
            answer.append(a[a_p])
            a_p += 1
        else:
            answer.append(b[b_p])
            b_p += 1
    
    print(' '.join(map(str, answer)))

## 처음에 푼 풀이
def solution1():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.extend(b)
    a.sort()
    for i in a : 
        print(i, end= ' ')

## 투포인터 방식을 응용하고자 시도해봤다. 그러나 solution1에서 시도한 방법 보다 시간이 더 오래걸림. 기본 정렬을 사용하자. 
def solution2():
    INF = 1e9 + 1
    n, m = map(int, input().split())
    a_list = deque(map(int, input().split()))
    b_list = deque(map(int, input().split()))
    answer = []
    a = INF
    b = INF
    while len(a_list) != 0 and len(b_list) != 0 :
        if(a==INF):
            a = a_list[0]
        if(b==INF):
            b = b_list[0]
        if a < b:
            answer.append(a)
            a_list.popleft()
            a = INF
        else :
            answer.append(b)
            b_list.popleft()
            b = INF
    
    if(a!=INF):
        answer.append(a)
        a_list.popleft()
    if(b!=INF):
        answer.append(b)
        b_list.popleft()
    
    if(len(a_list) != 0):
        answer.extend(a_list)
    
    if(len(b_list) != 0):
        answer.extend(b_list)
    for i in answer : 
        print(i, end= ' ')

solution()
