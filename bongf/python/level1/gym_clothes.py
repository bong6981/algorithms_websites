def solution(n, lost, reserve):
    to_remove = []
    for x in reserve :
        if x in lost :
            to_remove.append(x)
            lost.remove(x)
    
    for x in to_remove :
        reserve.remove(x)
    
    for x in reserve :
        if x-1 in lost :
            lost.remove(x-1)
        elif x+1 in lost :
            lost.remove(x+1)

    return n - len(lost)

n = 5 
lost = 	[2, 4]
reserve = [1, 3, 5]
print(solution(n, lost, reserve))