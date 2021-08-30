def solution(prices):
    answer = []
    for i in range(len(prices)-1) :
        time = 0 
        ## 마지막 인덱스일때는 if로 빼기 
        for j in range(i+1, len(prices)) :
            time += 1 
            if(prices[j] < prices[i]) :
                break
        answer.append(time)
    answer.append(0)
    return answer

print(solution([1, 2, 3, 2, 3]))
