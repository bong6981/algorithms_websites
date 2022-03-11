## https://programmers.co.kr/learn/courses/30/lessons/42898
def solution(m, n, puddles):
    graph = [[-1] * m for _ in range(n)]
    for puddle in puddles:
        x, y = puddle
        graph[y-1][x-1] = 0

    graph[0][0] = 1
    for x in range(1, m):
        if graph[0][x] == 0 :
            for y in range(x+1, m):
                graph[0][y] = 0
            break
        else:
            graph[0][x] = 1
    
    for x in range(1, n):
        if graph[x][0] == 0 :
            for y in range(x+1, n):
                graph[y][0] = 0
            break
        else:
            graph[x][0] = 1


    for i in range(n):
        for j in range(m):
            if graph[i][j] != -1:
                continue
            graph[i][j] = (graph[i][j-1] + graph[i-1][j]) % 1000000007

    return graph[n-1][m-1]

print(solution(4,3,[[2,2]]))

print(1000000008 % 1000000007)
