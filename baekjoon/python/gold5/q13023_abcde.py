## https://www.acmicpc.net/problem/13023
import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
graph = [[] for _ in range(N)] 

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

def search(start, arr):
    arr.append(start)

    if len(arr) == 5: 
        return True

    for des in graph[start]:
        if des in arr: continue
        if search(des, arr):
            return True
    arr.pop()
    return False

found = False
for i in range(N):
    if search(i, []):
        found = True
        print(1)
        break

if not found:
    print(0)

    

