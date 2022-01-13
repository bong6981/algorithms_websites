import sys
input = sys.stdin.readline

# https://www.acmicpc.net/problem/1976
def solution():
    global parents
    n = int(input())
    m = int(input())

    parents = [0] * (n) 
    for i in range(n):
        parents[i] = i  

    for now in range(n):
        des = list(map(int, input().split()))
        for i, to in enumerate(des):
            if to == 1 :
                union(now, i)
    
    trip = list(map(int, input().split()))
    for i in range(m-1):
        if find_p(trip[i]-1) != find_p(trip[i+1]-1) :
            return "NO"
    return "YES"            
    

def union(x, y):
    global parents
    x = find_p(x)
    y = find_p(y)

    if x < y :
        parents[y] = x
    else:
        parents[x] = y


def find_p(x):
    global parents
    if parents[x] != x :
        parents[x] = find_p(parents[x])
    return parents[x]

print(solution())
