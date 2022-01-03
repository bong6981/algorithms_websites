# https://www.acmicpc.net/problem/2417
def solution():
    x = int(input())
    x = x**(1/2)
    y = int(x)
    if y < x :
        print(y+1)
    else:
        print(y)
solution()
