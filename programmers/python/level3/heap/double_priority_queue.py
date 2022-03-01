# https://programmers.co.kr/learn/courses/30/lessons/42628
def solution_first(operations):
    queue = []
    for operation in operations:
        op, num = operation.split(" ")
        num = int(num)

        if op == "I":
            queue.append(num)
            for i in range(len(queue)-1, 0, -1):
                if queue[i] < queue[i-1] :
                    queue[i], queue[i-1] = queue[i-1], queue[i]
                else:
                    break
            
        else:
            if len(queue) == 0:
                continue
            if num == 1 :
                queue.pop()
            else:
                queue.pop(0)
            
    if len(queue) == 0:
        return [0, 0]
    return [queue[-1], queue[0]]        

import heapq
def solution(operations):
    max_heap = []
    min_heap = []
    nums = {}
    cnt = 0
    for operation in operations:
        op, num = operation.split(" ")
        print("===")
        num = int(num)

        if op == "I":
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            cnt += 1
            if num in nums:
                nums[num] += 1
            else:
                nums[num] = 1
            print(max_heap)
            print(min_heap)
            print(nums)
            
        else:
            if cnt == 0 :
                continue
            if num == 1 :
                n = (-1) * heapq.heappop(max_heap)
                while(nums[n] == 0):
                    n = (-1) * heapq.heappop(max_heap)
                nums[n] -= 1
                cnt-=1
                print(max_heap)
                print(min_heap)
                print(nums)
            else:
                n = heapq.heappop(min_heap)
                while(nums[n] == 0):
                    n = heapq.heappop(min_heap)
                nums[n] -= 1
                cnt-=1
                print(max_heap)
                print(min_heap)
                print(nums)
            
    if cnt == 0:
        return [0, 0]
    max_v = -heapq.heappop(max_heap)
    while(nums[max_v] == 0):
        max_v = -heapq.heappop(max_heap)
    min_v = heapq.heappop(min_heap)
    while nums[min_v] == 0:
        min_v = heapq.heappop(min_heap)
    return [max_v, min_v]


# print(solution(["I 16","D 1"]))
# print(solution(["I 7","I 5","I -5","D -1"]))
# print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
print(solution(["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"])) ## 문제1번만 틀릴 때 테케 
