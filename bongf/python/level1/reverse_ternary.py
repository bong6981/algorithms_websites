
def solution(n):
    result = ''
    while n > 0 :
        n, mod = divmod(n, 3)
        result += str(mod)
    
    while result[0] == '0' :
        result = result[1:]

    return sum( int(result[i]) * ( 3 ** (len(result) - 1 - i )) for i in range(len(result)))


def solution_2(n):
    result = ''
    while n:
        result += str(n%3)
        n = n//3 
    
    return int(result, 3)

print(solution_2(125))