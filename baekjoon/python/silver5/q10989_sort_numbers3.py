import sys
input = sys.stdin.readline



def sol_메모리초과():
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    for e in sorted(arr): print(e)
