import sys
input = sys.stdin.readline

# https://www.acmicpc.net/problem/15724
def solution():
    n, m = map(int, input().split())
    # graph는 계산의 편의를 위해 안쪽에 하나 더 그린다
    graph = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        row = list(map(int, input().split()))
        for j in range(1, m+1) :
            now = row[j-1]
            up = graph[i-1][j]
            left = graph[i][j-1]
            across = graph[i-1][j-1]
            graph[i][j] = up + left - across + now
    
    k = int(input())
    for _ in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        end = graph[x2][y2]
        up_to_subtract = graph[x1-1][y2]
        left_to_substract = graph[x2][y1-1]
        across_to_add = graph[x1-1][y1-1]
        print(end - up_to_subtract - left_to_substract + across_to_add)
        


# dp 가로에 대해서만 
def solution_fail_time_out():
    n, m = map(int, input().split())
    # graph는 계산의 편의를 위해 안쪽에 하나 더 그린다
    graph = [[0] * (m+1)]
    for _ in range(n):
        row = list(map(int, input().split()))
        now = 0
        accumalation = [0]
        for r in row : 
            now += r
            accumalation.append(now)
        graph.append(accumalation)
    
    k = int(input())
    
    answer = []
    for _ in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        cnt = 0
        for i in range(x2-x1+1) :
            cnt += graph[x1+i][y2] - graph[x1+i][y1-1]
        answer.append(cnt)
    for a in answer:
        print(a)

solution()


