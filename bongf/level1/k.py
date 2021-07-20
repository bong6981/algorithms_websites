def solution(array, commands):
    answer = []
    for x in commands :
        temp = array[x[0] - 1 : x[1]]
        temp = sorted(temp)
        answer.append(temp[x[2]-1])
        # i,j,k = x
        # answer.append(sorted(array[i-1:j])[k-1])
    return answer