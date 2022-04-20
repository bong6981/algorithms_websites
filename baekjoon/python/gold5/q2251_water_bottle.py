## https://www.acmicpc.net/problem/2251
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

import copy

A, B, C = map(int, input().rstrip().split())

capatiy = [A, B, C]
available = set()
did = set()


def dfs(now):
    global available, did
    if (now[0], now[1], now[2]) in did:
        return
    
    did.add((now[0], now[1], now[2]))
    if now[0] == 0:
        available.add(now[2])
    for i, v in enumerate(now):
        if v > 0:
            for j in range(3):
                if i == j:
                    continue
                ## 도착 물통에 다 채우거나, 내 물통에 비우거나  
                if capatiy[j] == now[j]:
                    continue
                if v +  now[j] <= capatiy[j]:
                    next = copy.deepcopy(now)
                    next[i] = 0
                    next[j] = v + now[j]
                    dfs(next)
                elif v > capatiy[j] - now[j]:
                    next = copy.deepcopy(now)
                    next[i] = v - (capatiy[j] - now[j])
                    next[j] = capatiy[j]
                    dfs(next)

                    
dfs([0, 0, capatiy[2]])

print(*sorted(list(available)))
                    

