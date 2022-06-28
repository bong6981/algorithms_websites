import sys

input = sys.stdin.readline

moves = [(-1, 1), (0, 1), (1, 1)]
R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(input().rstrip())

visited = [[0] * C for _ in range(R)]
path = []
ans = 0
    
def search(r, c, R, C):
    global visited
    visited[r][c] = 1
    if c == C - 1:
        return True

    for move in moves:
        nr = r + move[0]
        nc = c + move[1]
        if 0 <= nr < R and 0 <= nc < C:
            if not visited[nr][nc]:
                if board[nr][nc] != 'x':
                    if search(nr, nc, R, C) :
                        return True
    return False

for i in range(R):
    if search(i, 0, R, C):
        ans += 1

print(ans)
