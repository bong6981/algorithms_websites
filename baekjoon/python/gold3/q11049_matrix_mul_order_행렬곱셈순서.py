## https://www.acmicpc.net/problem/11049

def sol1():
    import sys
    sys.stdin = open('input.txt')
    input = sys.stdin.readline

    N = int(input().rstrip())

    dp = [[0] *(N+1) for _ in range(N+1)]

    for i in range(1, N+1):
        r, c = map(int, input().rstrip().split())
        dp[i][i] = (0, (r, c))


    def compare(a, b):
        av, apos = a
        bv, bpos = b
        if av >= bv :
            return b
        return a

    def cal(a, b):
        av, apos = a
        ar, ac = apos
        bv, bpos = b
        br, bc = bpos
        return (av + bv + ar * ac* bc, (ar, bc))


    for len in range(2, N+1):
        for i in range(1, N-len+2):
            j = i + len - 1
            dp[i][j] = (int(1e9), (0, 0))

            for k in range(i, j):
                dp[i][j] = compare(cal(dp[i][k], dp[k+1][j]), dp[i][j])

    print(dp[1][N][0])

def sol2():
    import sys
    sys.stdin = open('input.txt')
    input = sys.stdin.readline

    N = int(input().rstrip())

    dp = [[0] *(N+1) for _ in range(N+1)]
    matrix = [[0] * 2 for _ in range(N+1)]

    for i in range(1, N+1):
        r, c = map(int, input().rstrip().split())
        matrix[i][0] = r
        matrix[i][1] = c

    for len in range(2, N+1):
        for i in range(1, N-len+2):
            j = i + len - 1
            dp[i][j] = int(1e9)

            for k in range(i, j):
                dp[i][j] = min(dp[i][k] + dp[k+1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1], dp[i][j])

    print(dp[1][N])
        
        




