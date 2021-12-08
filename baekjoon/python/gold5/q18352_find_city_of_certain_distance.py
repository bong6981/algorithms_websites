## https://www.acmicpc.net/problem/18352
## 이전 풀이 : https://github.com/bong6981/algorithms_books/commit/d21b144cc795b5398b7c0513e77ebbd729178be0

import sys
input = sys.stdin.readline
from collections import deque


INF = 1e9

def solution():
    city_count, edge_count, target, start = map(int, input().split())
    distance = [-1] * (city_count+1)
    graph = [[] for _ in range(city_count+1)]
    for _ in range(edge_count):
        a, b = map(int, input().split())
        graph[a].append(b)
        
    distance[start] = 0
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        for des in graph[now]:
            if distance[des] != -1:
                continue
            distance[des] = distance[now]+1
            q.append(des)
    
    if target in distance:
        for i in range(city_count+1):
            if distance[i] == target:
                print(i)
    else:
        print(-1)


INF = 1e9

def solution_time_out():
    city_count, edge_count, target, start = map(int, input().split())
    distance = [INF] * (city_count+1)
    graph = [[] for _ in range(city_count+1)]
    for _ in range(edge_count):
        a, b = map(int, input().split())
        graph[a].append(b)

    distance[start] = 0
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        for des in graph[now]:
            distance[des] = min(distance[des], distance[now]+1)
            q.append(des)
    
    target_is = False
    for i, d in enumerate(distance):
        if d == target:
            print(i)
            target_is = True
    if not target_is:
        print(-1)
    

solution()



