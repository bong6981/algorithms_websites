import sys
input = sys.stdin.readline

# https://www.acmicpc.net/problem/1620
def solution():
    n, m = map(int, input().split())
    str_list = ['']
    str_dic = {}
    for i in range(1, n+1):
        string = input().rstrip()
        str_list.append(string)
        str_dic[string] = i
    
    for _ in range(m):
        string = input().rstrip()
        if string.isdigit():
            print(str_list[int(string)])
        else:
            print(str_dic[string])

solution()
