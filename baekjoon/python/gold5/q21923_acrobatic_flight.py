import sys
input = sys.stdin.readline
INF = int(1e9)

def sol1():
    n, m = map(int, input().split())
    points = [[0 for _ in range(m)] for _ in range(n)]
    ascending = [[0 for _ in range(m) for _ in range(n)]]
    decending = [[0 for _ in range(m) for _ in range(n)]]

    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(0, m):
            points[i][j] = row[j]

    ascending_points = [[-INF for _ in range(m)] for _ in range(n)]
    ascending_points[n-1][0] = points[n-1][0]
    for i in range(n-2, -1, -1):
        ascending_points[i][0] = points[i][0] + ascending_points[i+1][0]
    for i in range(1, m):
        ascending_points[n-1][i] = points[n-1][i] + ascending_points[n-1][i-1]
    for i in range(n-2, -1, -1):
        for j in range(1, m):
            ascending_points[i][j] = points[i][j] + max(ascending_points[i+1][j], ascending_points[i][j-1])

    decending_points = [[-INF for _ in range(m)] for _ in range(n)]
    decending_points[n-1][m-1] = points[n-1][m-1]
    for i in range(n-2, -1, -1):
        decending_points[i][m-1] = points[i][m-1] + decending_points[i+1][m-1]
    for i in range(m-2, -1, -1):
        decending_points[n-1][i] = points[n-1][i] + decending_points[n-1][i+1]
    for i in range(n-2, -1, -1):
        for j in range(m-2, -1, -1):
            decending_points[i][j] = points[i][j] + max(decending_points[i+1][j], decending_points[i][j+1])

    answer = -INF
    for i in range(n):
        for j in range(m):
            answer = max(answer, ascending_points[i][j] + decending_points[i][j])

    print(answer)

def sol2():
    import sys
    input = sys.stdin.readline
    INF = int(1e9)

    n, m = map(int, input().split())
    points = [[0 for _ in range(m+2)] for _ in range(n+2)]
    ascending = [[0 for _ in range(m+2)] for _ in range(n+2)]
    decending = [[0 for _ in range(m+2)] for _ in range(n+2)]

    for i in range(1, n+1):
        row = list(map(int, input().split()))
        for j in range(0, m):
            points[i][j+1] = row[j]

    for i in range(0, n+2, 1):
        for j in range(0, m+2, 1):
            ascending[i][j] = -INF
            decending[i][j] = -INF

    ascending[n][1] = points[n][1]
    decending[n][m] = points[n][m]

    for i in range(n, 0, -1):
        for j in range(1, m+1):
            if i == n and j == 1 : continue
            ascending[i][j] = points[i][j] + max(ascending[i+1][j], ascending[i][j-1])

    for i in range(n, 0, -1):
        for j in range(m, 0, -1):
            if i == n and j == m : continue
            decending[i][j] = points[i][j] + max(decending[i+1][j], decending[i][j+1])

    answer = -INF
    for i in range(1, n+1):
        for j in range(1, m+1):
            answer = max(answer, ascending[i][j] + decending[i][j])

    print(answer)

