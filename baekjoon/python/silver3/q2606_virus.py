from collections import deque
# https://www.acmicpc.net/problem/2606
def solution_second():
    c = int(input())
    board = [[] for _ in range(c+1)]
    for _ in range(int(input())):
        x, y = map(int, input().split())
        board[x].append(y)
        board[y].append(x)
    
    q = deque()
    ## visited = [0] * (c+1) 해줘서 자꾸 틀렸다.  0말고 이제 False로 하자
    # visited = [0 for _ in range(c+1)] 
    visited = [False] * (c+1)
    visited[1] = True
    cnt = 0
    q.append(1)
    
    while q:
        now = q.popleft()
        cnt += 1
        for x in board[now]:
            if visited[x] == False :
                visited[x] = True
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


def solution():
    import sys
    input = sys.stdin.readline

    cnt_com = int(input().rstrip())
    parent = list(range(cnt_com+1))

    def find_p(x):
        if parent[x] != x:
            parent[x] = find_p(parent[x])
        return parent[x]

    def union(x, y):
        x = find_p(x)
        y = find_p(y)
        if x < y :
            parent[y] = x
        else:
            parent[x] = y


    for _ in range(int(input().rstrip())):
        x, y = map(int, input().rstrip().split())
        union(x, y)

    for i in range(1, cnt_com+1):
        find_p(i)

    print(parent.count(parent[1])-1)


print(solution())
