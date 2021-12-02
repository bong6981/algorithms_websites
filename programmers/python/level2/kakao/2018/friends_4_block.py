## https://programmers.co.kr/learn/courses/30/lessons/17679
## 카카오 블라인드 2018
def solution(m, n, board):
    graph = []
    for b in board:
        graph.append(list(b))

    moves = [(0, 1), (1, 0), (1,1)]

    cnt = 0
    while True:
        to_delete = []
        for i in range(m):
            for j in range(n):
                if graph[i][j] != '':
                    now = graph[i][j]
                    now_list = [(i, j)]
                    for move in moves :
                        ni = i + move[0]
                        nj = j + move[1]
                        if not ((0<= ni <m) and (0<=nj<n)):
                            break
                        if not (graph[ni][nj] == now):
                            break
                        now_list.append((ni, nj))
                    if len(now_list) == 4:
                        to_delete.append(now_list)
        
        if to_delete == []:
            break
        for delete_list in to_delete:
            for x, y in delete_list:
                if graph[x][y] != '' :
                    cnt += 1
                    graph[x][y] = ''
        
        empty_list = []
        for i in range(m-1, -1, -1):
            for j in range(n):
                if j not in empty_list:
                    if graph[i][j] == '' :
                        empty = True
                        for k in range(i-1, -1, -1):
                            if graph[k][j] != '':
                                graph[i][j], graph[k][j] = graph[k][j], graph[i][j]
                                empty = False
                                break
                        if empty:
                            empty_list.append(j)
    
    return cnt




print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
