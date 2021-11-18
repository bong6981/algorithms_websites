## 효율성 실패
def solution_fail(scoville, K):
    scoville.sort()
    count = 0
    while scoville[0] < K :
        if len(scoville)==1 :
            return -1
        scoville[1] = scoville[0] + scoville[1] * 2
        scoville = scoville[1::]
        scoville.sort()
        count += 1
    return count


import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    c = 0
    while scoville[0] < K:
        if(len(scoville)) == 1:
            return -1
        n = heapq.heappop(scoville)
        m = heapq.heappop(scoville)
        heapq.heappush(scoville, n + m*2)
        c += 1
    return c
    

print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([1, 2, 3],11))
print(solution([2, 3, 7, 10, 15],11))




# print(solution([1, 2, 3, 9, 10, 12], 7))

