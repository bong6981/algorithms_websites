# https://www.acmicpc.net/problem/21606
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input().rstrip())

graph = [[] for _ in range(N+1)]


def success_from_other():
    in_out = '0' + input().rstrip()
    for _ in range(N-1):
        x, y = map(int, input().rstrip().split())
        graph[x].append(y)
        graph[y].append(x)


    def dfs(start):
        visited[start] = 1
        ret = 0
        for des in graph[start]:
            if not visited[des]:
                if in_out[des] == '1':
                    ret += 1
                else:
                    ret += dfs(des)
        return ret

    ans = 0    
    visited = [0] * (N+1)
    for i in range(1, N+1):
        c = in_out[i]
        if c == '1':
            for des in graph[i]:
                if in_out[des] == '1':
                    ans += 1
        else:
            if not visited[i]:
                ret = dfs(i)
                ans += ret * (ret-1)
    print(ans)
success_from_other()

def fail():
    in_out = [0] * (N+1) ## 1이 실내 
    in_points = []
    for i, c in enumerate(input().rstrip()):
        c = int(c)
        in_out[i+1] = c
        if c == 1: 
            in_points.append(i+1)
    for _ in range(N-1):
        x, y = map(int, input().rstrip().split())
        graph[x].append(y)
        graph[y].append(x)

    def sol(start, cnt):
        visited[start] = 1
        for des in graph[start]:
            if not visited[des]:
                if in_out[des]:
                    visited[des] = 1
                    cnt += 1
                else:
                    cnt = sol(des, cnt)
        return cnt

    ans = 0
    for start in in_points:
        visited = [0] * (N+1)
        ans += sol(start, 0)

    print(ans)

# fail()





