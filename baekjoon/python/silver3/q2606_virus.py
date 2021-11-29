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

'''
원래 풀이는 입력값이 아래와 같이 들어갈 경우
if find_p(parent, i) == 1: 
이 부분을 그냥 parent[i]로 해서 값이 가장 작은 부모를 향하도록 초기화가 되지 않았기 때문에
3
2
2 3
1 2
[0, 1, 1, 2] 가 되어 답을 틀린다.
맞게 고치어 test 통과!
이 풀이가 위에 풀이보다 메모디나 시간 면에서 아주 조금 더 낫다.
'''
def solution():
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
        if find_p(parent, i) == 1:
            cnt += 1
    return cnt

print(solution())
