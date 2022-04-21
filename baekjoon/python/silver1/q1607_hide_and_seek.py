# 5:36
from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
MAX_TIME = int(10**6)
ans = MAX_TIME

q = deque([(K, 0)])
visited = set()

while q:
    now, time = q.popleft()
    if now == N:
        print(time)
        break
    dests = [now+1]
    if now -1 > 0:
        dests.append(now - 1)
    if now % 2 == 0:
        dests.append(now // 2)
    for des in dests:
        if  des not in visited:
            visited.add(des)
            q.append((des, time+1))




