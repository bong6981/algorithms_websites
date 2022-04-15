import sys, heapq
input = sys.stdin.readline

N = int(input())
buildngs = []
for _ in range(N):
    L, H, R = map(int, input().split())
    buildngs.append((L, -H, R))
    buildngs.append((R, H, L)) ## H가 같으면 L이 먼저온다
buildngs.sort()

p = []
now = 0
ans = []
end = set()
for d, h, opposite in buildngs:
    if h < 0:
        if now < -h:
            now = -h
            ans.append((d, now))
        heapq.heappush(p, (-h, opposite))
    else:
        end.add(d)
        while p:
            if p[0][1] not in end:
                break
            heapq.heappop(p)
        
        if not p:
            if now:
                now = 0
                ans.append((d, 0))
        else:
            if -p[0][0] != now:
                now = -p[0][0]
                ans.append((d, now))
for e in ans:
    print(e[0], e[1], end=' ')


