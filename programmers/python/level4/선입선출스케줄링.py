import heapq


def solution(n, cores):
    if n <= len(cores):
        return n

    start = 0
    end = max(cores) * n

    checked_time = 0
    checked_cnt = 0

    while start <= end:
        mid = (start + end) // 2

        ## 마지막에 들어갈 곳의 index를 알아야 하므로 len(cores) 보다 적개 채웠을 때 몇초인지 구한다 
        cnt = len(cores)

        for core in cores:
            cnt += (mid // core)

        if cnt >= n:
            end = mid -1 
        else:
            checked_time = mid
            checked_cnt = cnt
            start = mid + 1

    ## 남은 개수는 checked_cnt를 빼고, 이제 checked_time+1 초에 다 들어갈 수 있으므로 len(cores)를 한 번 더 빼준다. 
    ## 어차피 checked_cnt + len(cores)가 n보다 작을 때로 구했으므로 left는 항상 양수다 
    left = n - checked_cnt
    checked_time += 1

    ## 이제 하나씩 넣어준다. 
    for idx, core in enumerate(cores):
        if checked_time % core == 0:
            left -= 1
            if left == 0:
                return idx + 1

    



# def solution(n, cores):
#     if n <= len(cores):
#         return n
    
#     q = []
#     for i, v in enumerate(cores):
#         heapq.heappush(q, (v, i))

#     t = 0    
#     for i in range(len(cores)+1, n+1):
#         complete_time, index = heapq.heappop(q)
#         t = complete_time
#         heapq.heappush(q, (t+cores[index], index))
#         if i == n:
#             return index+1

print(solution(6, [1,2,3]))


