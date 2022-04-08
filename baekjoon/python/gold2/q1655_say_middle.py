#11:49
## https://www.acmicpc.net/problem/1655
import heapq
import sys
input = sys.stdin.readline

n = int(input())
max_heap = []
min_heap = []

for _ in range(n):
    num = int(input())
    if len(max_heap) == len(min_heap):
        ##  max 힙에 넣는다 
        if len(min_heap) != 0 and min_heap[0] < num:
            to_move = heapq.heappop(min_heap)
            heapq.heappush(max_heap, (-to_move, to_move))
            heapq.heappush(min_heap, num)
        else:
            heapq.heappush(max_heap, (-num, num))
    else:
        ## min 힙에 넣는다
        if len(max_heap) != 0 and max_heap[0][1] > num:
            heapq.heappush(min_heap, heapq.heappop(max_heap)[1])
            heapq.heappush(max_heap, (-num, num))
        else:
            heapq.heappush(min_heap, num)
    print(max_heap[0][1])

