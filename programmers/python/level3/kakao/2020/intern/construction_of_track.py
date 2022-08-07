## https://school.programmers.co.kr/learn/courses/30/lessons/67259
from collections import deque

def cal(price, d, new_d):
    if (d == 0 or d == 1) and (new_d == 2 or new_d == 3):
        return price + 600
    if (d == 2 or d == 3) and (new_d == 0 or new_d == 1):
        return price + 600
    return price + 100 

def solution(board):
    board_size = len(board)
    # 하 0, 상 1, 좌2, 우3
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    routes = deque([])
    board[0][0] = [0, 0, 0, 0]
    routes.append((0, 0, 0, 3))
    routes.append((0, 0, 0, 0))
    
    #price, dir
    ans = -1
    
    while routes:
        r, c, price, d = routes.popleft()
        for idx, move in enumerate(moves):
            nr = r + move[0]
            nc = c + move[1]
            
            if 0 <= nr < board_size and 0 <= nc < board_size:
                if board[nr][nc] != 1:
                    new_price = cal(price, d, idx)

                    if nr == board_size - 1 and nc == board_size -1:
                        if ans == -1:
                            ans = new_price
                        else:
                            ans = min(ans, new_price)
                    else:
                        if board[nr][nc] == 0: #한번도 방문 안했을 때
                            board[nr][nc] = [-1, -1, -1, -1]
                        
                        if board[nr][nc][idx] == -1 or board[nr][nc][idx] > new_price:
                            board[nr][nc][idx] = new_price
                            routes.append((nr, nc, new_price, idx))
    return ans


print(solution([[0,0,0],[0,0,0],[0,0,0]]))
# print(solution([[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 1], [0, 1, 1, 0, 0]]))
# print(solution([
# [0, 0, 0, 0, 0],
# [0, 1, 1, 1, 0],
# [0, 0, 1, 0, 0],
# [1, 0, 0, 0, 1],
# [0, 1, 1, 0, 0]
# ]))
