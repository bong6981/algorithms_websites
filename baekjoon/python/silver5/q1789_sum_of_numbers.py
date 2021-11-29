## https://www.acmicpc.net/problem/1789
def solution():
    n = int(input())
    total = 0
    now = 0
    while(total<n):
        now += 1
        total += now
    if total != n :
        now -= 1
    return now

print(solution())

## 이분 탐색으로 푼 풀이를 찾아봄
def other():
    n = int(input())
    start = 1
    end = n

    while start <= end :
        mid = (start + end) // 2
        if mid * (mid+1) // 2 <= n :
            answer = mid
            start = mid + 1
        else:
            end = mid-1
    return answer

print(other)

## 근의 공식 이용해서 푼 풀이도 있다. 
