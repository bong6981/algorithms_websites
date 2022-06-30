import sys
input = sys.stdin.readline
from collections import deque

N, C = map(int, input().split())
M = int(input())
packages = []
tmp = []
for i in range(M):
    send, receive, cnt = map(int, input().split())
    packages.append((send, receive, cnt))
    tmp.append((receive, i))


tmp.sort()
tmp = deque(tmp)

ret = [C] * N
ans = 0

for diff, idx in tmp:
    send, receive, cnt = packages[idx]

    val = min(ret[send:receive])
    if val > 0:
        if cnt < val:
            val = cnt
        ans += val
        for i in range(send, receive):
            ret[i] -= val

print(ans)
