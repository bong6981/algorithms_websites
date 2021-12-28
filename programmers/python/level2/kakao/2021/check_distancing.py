# https://programmers.co.kr/learn/courses/30/lessons/81302?language=java
from collections import deque
def solution2(places):
    answer = []
    for p in places:
        answer.append(get_answer_solution2(p))
    return answer

def get_answer_solution2(p):
    for i in range(5):
        for j in range(5):
            if p[i][j] == 'P':
                if not bfs(p, i, j) :
                    return 0
    return 1

def bfs(p, i, j):
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque([(i, j, 0)])
    visited = [[False] * 5 for _ in range(5)]
    while q :
        i, j, d = q.popleft()
        visited[i][j] = True
        for m in move :
            ni = i + m[0]
            nj = j + m[1]
            nd = d + 1

            if 0<= ni < 5 and 0<= nj < 5 :
                if not visited[ni][nj]:
                    visited[ni][nj] = True
                    if p[ni][nj] == 'P':
                        return False
                    if p[ni][nj] == 'O' and nd == 1:
                        q.append((ni, nj, nd))
    return True

def solution1(places):
    answer = []
    for p in places:
        answer.append(get_answer_solution1(p))
    return answer

def get_answer_solution1(p):
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in range(5):
        for j in range(5):
            if p[i][j] == 'P':
                for m in move :
                    ni = i + m[0]
                    nj = j + m[1]
                    if 0 <= ni <= 4 and 0 <= nj <= 4 :
                        if p[ni][nj] == 'P' :
                            return 0
            if p[i][j] == 'O':
                cnt = 0
                for m in move :
                    ni = i + m[0]
                    nj = j + m[1]
                    if 0 <= ni <= 4 and 0 <= nj <= 4 :
                        if p[ni][nj] == 'P' :
                            cnt += 1
                if cnt >= 2:
                    return 0 
    return 1


def get_answer_fail_13(p):
    for i in range(5):
        for j in range(5):
            if p[i][j] == 'P':
                if check(p, (i, j)) == 0 :
                    return 0
    return 1

def check(p, start) :
    x, y = start
    if y+1 < 5 and p[x][y+1] != 'X':
        if check_right(p, start) == 0:
            return 0
    if x+1 < 5 and p[x+1][y] != 'X':
        if check_down(p, start) == 0:
            return 0
    if x+1 < 5 and y + 1 < 5 and (p[x][y+1] != 'X' or p[x+1][y] != 'X'):
        if check_right_down(p, start) == 0:
            return 0
    if x+1 < 5 and y -1 > 0 and (p[x][y-1] != 'X' or p[x+1][y]) != 'X':
        if check_left_down(p, start) == 0:
            return 0

def check_right(p, start):
    x, y = start
    if p[x][y+1] == 'P':
        return 0
    if y+2 < 5 and p[x][y+2] == 'P':
        return 0
    return 1 

def check_down(p, start):
    x, y = start
    if p[x+1][y] == 'P':
        return 0
    if x+2 < 5 and p[x+2][y] == 'P':
        return 0
    return 1 

def check_right_down(p, start):
    x, y = start
    if p[x+1][y+1] == 'P':
        return 0
    return 1

def check_left_down(p, start):
    x, y = start
    if p[x+1][y-1] == 'P':
        return 0
    return 1

# print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
# print(solution([["OOPOO", "OPOOO", "OOOOO", "OOOOO", "OOOOO"]]))

