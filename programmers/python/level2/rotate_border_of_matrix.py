def solution(rows, columns, queries):
    graph = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            graph[i][j] = i * columns + j + 1

    answer = []

    for query in queries :
        x1, y1, x2, y2 = query
        x1 = x1 -1 
        y1 = y1 -1 
        x2 = x2 -1
        y2 = y2 -1 
        c = y2 - y1 
        r = x2 - x1 

        prev = graph[x1][y1]
        min_num = 1e9
        for i in range(y1+1, y1+1+c):
            min_num = min(min_num, prev)
            temp = graph[x1][i]
            graph[x1][i] = prev
            prev = temp
         

        for i in range(x1+1, x1+1+r):
            min_num = min(min_num, prev)
            temp = graph[i][y2]
            graph[i][y2] = prev
            prev = temp
   
        
        for i in range(y2-1, y2-1-c, -1):
            min_num = min(min_num, prev)
            temp = graph[x2][i]
            graph[x2][i] = prev
            prev = temp
   
        
        for i in range(x2-1, x2-1-r, -1):
            min_num = min(min_num, prev)
            temp = graph[i][y1]
            graph[i][y1] = prev
            prev = temp
     
        answer.append(min_num)
    return answer

def solution2(rows, columns, queries):
    answer = []

    ## 배열 초기화 
    board = [[i+j*columns for i in range(1, columns+1)] for j in range(rows)]
    ## 바로 a,b,c,d로 받기 
    for a, b, c, d in queries:
        r1, c1, r2, c2 = a-1, b-1, c-1, d-1

        ## stack 활용하기 
        stack = []
        for i in range(c1, c2+1):
            stack.append(board[r1][i])
            if len(stack) == 1:
                continue
            else :
                board[r1][i] = stack[-2]
        
        for j in range(r1+1, r2+1):
            ## 위에서 남은 i값 그대로 활용하기 
            stack.append(board[j][i])
            board[j][i] = stack[-2]
        
        for k in range(c2-1, c1-1, -1):
            stack.append(board[j][k])
            board[j][k] = stack[-2]

        for l in range(r2-1, r1-1, -1):
            stack.append(board[l][k])
            board[l][k] = stack[-2]
        
        ## 스택에 값 쌓이니까 가능 
        answer.append(min(stack))

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
# print(solution2(3,3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
# print(solution(100, 97, [[1,1,100,97]]))

