## https://www.acmicpc.net/workbook/view/7942
def sol():
    import sys
    input = sys.stdin.readline
    lab = []

    n, m = map(int, input().split())
    fan = []
    for r in range(n):
        row = list(map(int, input().split()))
        for c in range(m):
            if row[c] == 9:
                fan.append((r, c))
        lab.append(row)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


    # 상 0, 하 1, 좌 2, 우3
    def change_dir(obj, dir):
        if obj == 1 :
            if dir == 2 :
                return -1
            if dir == 3:
                return -1
        
        if obj == 2:
            if dir == 0:
                return -1
            if dir == 1:
                return -1
        
        if obj == 3:
            if dir == 0:
                return 3
            if dir == 1:
                return 2
            if dir == 2:
                return 1
            if dir == 3:
                return 0
        if obj == 4:
            if dir == 0:
                return 2
            if dir == 1:
                return 3
            if dir == 2:
                return 0
            if dir == 3:
                return 1
        return dir

    visited = [[0 for _ in range(m)] for _ in range(n)]
    def blow(i, j, dir):
        while True:
            visited[i][j] = True
            if dir == -1 :
                break
            i += moves[dir][0]; j+= moves[dir][1]
            if not ((0 <= i <n) and (0<= j < m)) : break
            if lab[i][j] == 9: break
            if lab[i][j] >= 1 : dir = change_dir(lab[i][j], dir)

    for f in fan :
        for i in range(4) :
            nx = f[0]
            ny = f[1]
            dir = i
            blow(nx, ny, dir)
    print(sum(map(sum, visited)))

sol()

def sol_time_out():
    import sys
    input = sys.stdin.readline
    lab = []

    n, m = map(int, input().split())
    fan = []
    for r in range(n):
        row = list(map(int, input().split()))
        for c in range(m):
            if row[c] == 9:
                fan.append((r, c))
        lab.append(row)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    ans = 0

    # 상 0, 하 1, 좌 2, 우3
    def change_dir(obj, dir):
        if obj == 1 :
            if dir == 2 :
                return 3
            if dir == 3:
                return 2
            return dir
        
        if obj == 2:
            if dir == 0:
                return 1
            if dir == 1:
                return 0
            return dir
        
        if obj == 3:
            if dir == 1:
                return 2
            if dir == 3:
                return 0
            if dir == 2:
                return 1
            return 3
        
        if dir == 2:
            return 0
        
        if dir == 1:
            return 3
        
        if dir == 3:
            return 1
        return 2

    visited = [[[0 for _ in range(5)] for i in range(m)] for _ in range(n)]
    def blow(i, j, d):
        global ans
        while True:
            if visited[i][j][d] :
                break
            visited[i][j][d] = True
            if not visited[i][j][4] :
                visited[i][j][4] = True
                ans += 1

            i += moves[d][0]; j+= moves[d][1]
            if not ((0 <= i <n) and (0<= j < m)) or lab[i][j] == 9: break
            if lab[i][j] >= 1 : d = change_dir(lab[i][j], d)


    for f in fan :
        for i in range(4) :
            nx = f[0]
            ny = f[1]
            dir = i
            blow(nx, ny, dir)
    print(ans)

