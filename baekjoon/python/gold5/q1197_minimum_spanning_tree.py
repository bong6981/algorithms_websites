## https://www.acmicpc.net/problem/1197

import sys
input = sys.stdin.readline
global parent

def solution():
    global parent
    v, e = map(int, input().rstrip().split())
    parent = [0] * (v+1)
    
    for i in range(v+1):
        parent[i] = i
    
    edges = []
    result = 0 
    for i in range(e):
        a, b, c = map(int, input().rstrip().split())
        edges.append((c, a, b))
    
    edges.sort()
    for e in edges:
        c, a, b = e
        if find_p(a) != find_p(b):
            union(a, b)
            result += c
    
    return result

def find_p(x):
    global parent
    if parent[x] != x :
        parent[x] = find_p(parent[x])
    return parent[x]

def union(x, y):
    global parent
    x = find_p(x)
    y = find_p(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y 

print(solution())
