## https://www.acmicpc.net/problem/13334

import heapq
import sys
input = sys.stdin.readline

def sol():
    n = int(input())
    ans = 0
    positions = [] 
    for _ in range(n):
        p1, p2 = map(int, input().split())
        positions.append((min(p1, p2), max(p1, p2)))

    positions.sort(key = lambda x: (x[1], x[0]))
    d = int(input())

    ans = 0

    acc = []
    for i in range(n): 
        next_s, next_e = positions[i]
        if next_e - next_s > d :
            continue

        if not acc :
            acc.append(positions[i])

        else:
            while next_e - acc[0][0] > d: 
                heapq.heappop(acc)
                if not acc :
                    break
        
            heapq.heappush(acc, (next_s, next_e))

        ans = max(ans, len(acc))

    print(ans)

sol()
