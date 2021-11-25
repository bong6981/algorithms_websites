from collections import deque
# https://www.acmicpc.net/problem/2606
def solution():
    c = int(input())
    board = [[] for _ in range(c+1)]
    for _ in range(int(input())):
        x, y = map(int, input().split())
        board[x].append(y)
        board[y].append(x)
    
    q = deque()
    ## visited = [0] * (c+1) 해줘서 자꾸 틀렸다. 
    visited = [0 for _ in range(c+1)] 
    visited[1] = 1
    cnt = 0
    q.append(1)
    
    while q:
        now = q.popleft()
        cnt += 1
        for x in board[now]:
            if visited[x] == 0 :
                visited[x] = 1
                q.append(x)
    return cnt -1



def find_p(parent, x):
    if parent[x] != x :
        parent[x] = find_p(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x = find_p(parent, x)
    y = find_p(parent, y)
    if x < y :
        parent[y] = x
    else : 
        parent[x] = y

## 이렇게 풀었을 경우에 
'''
입력값이 아래와 같이 들어갈 경우 
3
2
2 3
1 2
[0, 1, 1, 2] 가 되어 답을 틀린다.
'''
def solution_fail():
    c = int(input())
    edges_num = int(input())

    parent = [0] * (c+1)
    for i in range(1, c+1):
        parent[i] = i

    for _ in range(edges_num):
        x, y = map(int, input().split())
        if(find_p(parent, x) != find_p(parent, y)):
            union(parent, x, y)
    cnt = 0
    for i in range(2, c+1):
        if parent[i] == 1:
            cnt += 1
    print(parent)
    return cnt

print(solution())
