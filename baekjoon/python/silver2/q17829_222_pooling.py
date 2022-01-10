import sys
input = sys.stdin.readline

# https://www.acmicpc.net/problem/17829
def solution():
    n = int(input())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))

    while n > 2 : 
        n, board = change(n, board)
    
    answer = []
    for i in range(2):
        for j in range(2):
            answer.append(board[i][j])
    answer.sort(reverse=True)
    return answer[1]

def change(n, board):
    idxs = [ i for i in range(0, n-1, 2)]
    new_board = [] 
    for i, x in enumerate(idxs):
        temp1 = []
        for y in idxs:
            temp2 = []
            temp2.append(board[x][y])
            temp2.append(board[x][y+1])
            temp2.append(board[x+1][y+1])
            temp2.append(board[x+1][y])
            temp2.sort(reverse=True)
            temp1.append(temp2[1])
        new_board.append(temp1)
    return n//2, new_board
        
print(solution())


n=int(input())
m=[[*map(int,input().split())]for i in range(n)]
while n>1:
    n//=2
    m2=[n*[0]for i in range(n)]
    for i in range(n):
        for j in range(n):
            m2[i][j]=sorted([m[2*i][2*j],m[2*i][2*j+1],m[2*i+1][2*j],m[2*i+1][2*j+1]])[2]
    m=m2
    print(m2)
print(*m[0])
