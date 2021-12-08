## https://www.acmicpc.net/problem/1717
## setrecurtionlimt 과 stdin.readline 해줘야 통과
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    parents = []
    for i in range(n+1):
        parents.append(i)
    
    def find_p(x):
        if parents[x] != x:
            parents[x] = find_p(parents[x])
        return parents[x]


    def union(x, y):
        x = find_p(x)
        y = find_p(y)
        if x < y :
            parents[y] = x 
        else:
            parents[x] = y

    for _ in range(m):
        op, a, b = map(int, input().split())
        if op == 0 :
            union(a, b)
        else:
            if find_p(a) == find_p(b):
                print("YES")
            else: 
                print("NO")

solution()


def solution_memory_exceeded():
    n, m = map(int, input().split())
    sets = []
    for i in range(n+1):
        sets.append({i})
    for _ in range(m):
        op, a, b = map(int, input().split())
        if op == 0 : 
            if sets[a] != sets[b]:
                hap = sets[a] | sets[b]
                for i in hap:
                    sets[i] = hap
        if op == 1:
            if sets[a] == sets[b] :
                print("YES")
            else:
                print("NO")


        


