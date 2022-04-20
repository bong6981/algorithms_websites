## https://www.acmicpc.net/problem/14226
from collections import deque
import sys
input = sys.stdin.readline

S = int(input().rstrip())

display = 1
clip = 0
time = 0
q = deque([(display, clip, time)])
visited = set()
visited.add((1, 0))


while q:
    display, clip, time = q.popleft()

    if display == S:
        print(time)
        break
    
    #복사, 삭제
    if display > 0:
        if (display, display) not in visited:
            q.append((display, display, time+1))
            visited.add((display, display))
        if (display-1, clip) not in visited:
            q.append((display-1, clip, time+1))
            visited.add((display-1, clip))
    
    # 붙여넣기 
    if clip > 0:
        if (display+clip, clip) not in visited:
            q.append((display+clip, clip, time+1))
            visited.add((display+clip, clip))

    

