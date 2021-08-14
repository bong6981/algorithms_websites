def solution(board, moves):
    answer = 0
    result = [] 
    for i in moves :
        for j in range(len(board)) :
            if board[j][i-1] != 0 :
                if len(result) != 0 and result[len(result) -1] ==  board[j][i-1]:
                    result = result[:len(result) -1]
                    answer += 2
                    board[j][i-1] = 0
                    break
                else :
                    result.append(board[j][i-1])
                    board[j][i-1] = 0
                    break
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]	
print(solution(board, moves))