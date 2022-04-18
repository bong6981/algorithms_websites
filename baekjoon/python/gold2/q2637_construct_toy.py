## https://www.acmicpc.net/problem/2637
from collections import deque
import sys
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())

parts = [[] for _ in range(N+1)]
indegree = [0] * N
end = []
for _ in range(M):
    X, Y, K = map(int, input().split())
    if X == N:
        end.append((Y, K))
    else:
        parts[Y].append((X, K))
        indegree[X] += 1

q = deque()
for i in range(N):
    if indegree[i] == 0:
        q.append(i)

def add_p(p_info, x, now_ele, cnt):
    if now_ele in p_info[x]:
        p_info[x][now_ele] += cnt
    else:
        p_info[x][now_ele] = cnt

p_info = [{} for _ in range(N)]
while q:
    now = q.popleft()
    ## now가 기본 부품일 때 
    now_info = {now : 1}
    if p_info[now] != {}:
        now_info = p_info[now]
    
    for x, k in parts[now]:
        # x는 now가 k필요한 제품
        for now_ele in now_info: 
            add_p(p_info, x, now_ele, now_info[now_ele] * k) ## 여기 갯수 합쳐주는 것으로 정리
        
        indegree[x] -= 1
        if indegree[x] == 0:
            q.append(x)

def add_p_for_end(ans, ele, cnt):
    if ele in ans:
        ans[ele] += cnt
    else:
        ans[ele] = cnt 



ans = {}
for ele, cnt in end:
    if p_info[ele] != {}:
        for p_p_ele in p_info[ele]:
            add_p_for_end(ans, p_p_ele, p_info[ele][p_p_ele] * cnt)
    else:
        add_p_for_end(ans, ele, cnt)

index = list(ans)
index.sort()
for i in index:
    print(i, ans[i])








## 메모리 초과 풀이 
def memeory_overflow():
    q = deque()
    for _ in range(M):
        X, Y, K = map(int, input().split())
        if X == N:
            q.append((Y, K))
        else:
            parts[X].append((Y, K))

    p_info = [0] * (N+1)
    while q:
        part, cnt = q.popleft()
        if parts[part] == []:
            p_info[part] += cnt
        else:
            for p_p, p_cnt in parts[part]:
                q.append((p_p, p_cnt*cnt))

    for i in range(1, len(p_info)):
        if p_info[i] != 0:
            print(i, p_info[i])
        


