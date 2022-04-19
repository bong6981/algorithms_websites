## https://www.acmicpc.net/problem/9470
from collections import deque
from collections import Counter
import sys
input = sys.stdin.readline

T = int(input().rstrip())

for t in range(1, T+1):
    K, M, P = map(int, input().rstrip().split())
    graph = [[] for _ in range(M+1)]
    indegree = [0] * (M+1)
    cost = [[] for _ in range(M+1)]
    cost_r = [0] * (M+1)

    for _ in range(P):
        x, y = map(int, input().rstrip().split())
        graph[x].append(y)
        indegree[y] += 1
    
    q = deque()
    for i in range(1, M+1):
        if indegree[i] == 0:
            cost_r[i] = 1
            q.append(i)
    
    while q:
        now = q.popleft()
        if cost[now] != []:
            cnt = Counter(cost[now])
            eles = set(cost[now])
            ans = [0, 0] # 값, 개수
            for c in eles:
                if ans[0] < c: 
                    ans = [c, cnt[c]]
            if ans[1] >= 2:
                ans[1] = ans[0] + 1
            else:
                ans[1] = ans[0]
            cost_r[now] = ans[1]

        for des in graph[now]:
            indegree[des] -= 1
            cost[des].append(cost_r[now])
            if indegree[des] == 0:
                q.append(des)
            
    print(t, cost_r[M])
        

