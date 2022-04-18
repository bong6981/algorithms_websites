from collections import deque
import sys
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
indegree = [0] * (N+1)
go_board = [[] for _ in range(N+1)]
return_board = [[] for _ in range(N+1)]

for _ in range(M):
    S, E, C = map(int, input().rstrip().split())
    go_board[S].append((E, C))
    return_board[E].append((S, C))
    indegree[E] += 1

START, DEST = map(int, input().rstrip().split())
q = deque()
q.append((START, 0))

path = [0] * (N+1)

while q:
    now, cost = q.popleft()
    for des, des_c in go_board[now]:
        new_cost = cost + des_c
        if new_cost > path[des]:
            path[des] = new_cost
        
        indegree[des] -= 1
        if indegree[des] == 0:
            q.append((des, path[des]))


print(path[DEST])

q = deque([DEST])
cnt = 0
visited = [0] * (N+1)

while q: 
    now = q.popleft()
    for prev, prev_cost  in return_board[now]:
        if path[now] - prev_cost  == path[prev]:
            cnt += 1
            if not visited[prev]:
                q.append(prev)
                visited[prev] = 1 

print(cnt)

            


