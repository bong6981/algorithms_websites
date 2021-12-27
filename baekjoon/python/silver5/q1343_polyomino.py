# https://www.acmicpc.net/problem/1343
def solution():
    board = input()
    answer = []
    delimiter = False
    if board[0] == '.':
        delimiter = True
    string = board[0]
    for i, block in enumerate(board):
        if i == 0:
            continue
        if delimiter :
            if block == '.':
                string += block
            else:
                answer.append(string)
                string = block
                delimiter = False
        else:
            if block == '.':
                ans = pick(string)
                if ans == -1 :
                    return -1
                answer.append(ans)
                string = block
                delimiter = True
            else:
                string += block

    if delimiter :
        answer.append(string)
    else:
        ans = pick(string)
        if ans == -1 :
            return -1
        answer.append(ans)
    return "".join(answer)

def pick(string):
    answer = ''
    a = 'AAAA'
    b = 'BB'
    mock, rest = divmod(len(string), 4)
    for _ in range(mock):
        answer += a
    if rest % 2 != 0 :
        return -1 
    if rest == 0:
        return answer
    answer += b
    return answer

print(solution())


# 백준 id : jh05013 (파이썬 랭커)
def solution_other():
    s = input().replace("XXXX","AAAA").replace("XX","BB")
    print(s if "X" not in s else -1)
