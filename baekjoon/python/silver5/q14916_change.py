## https://www.acmicpc.net/problem/14916
def solution() :
    n = int(input())
    max_five = n // 5
    cnt = 0
    while max_five >= 0:
        temp = n 
        temp -= max_five * 5
        if(temp %2 == 0):
            cnt = max_five + temp // 2
            break
        max_five -= 1
    if max_five < 0 :
        return -1
    return cnt

print(solution())
