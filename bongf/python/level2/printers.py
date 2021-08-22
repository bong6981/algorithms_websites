def solution(priorities, location):
    count = 0 
    while True :
        max_index = priorities.index(max(priorities))
        if(location < max_index) :
            location = len(priorities) -1 - max_index + location  
        elif(location == max_index) :
            return count+1
        else : 
            location -= (max_index+1)
        priorities = priorities[max_index+1:] + priorities[0:max_index]
        count += 1

    return count

## popleft()대신 pop(0)을 쓸 수 있으나, list의 마지막까지 가는 것이라 시간 복잡도가 너무 많이 소요된다. 
## popleft()를 써주자 
from collections import deque 
def solution2(priorities, location):
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    answer = 0

    while True :
        cur = queue.popleft()
        if any(cur[1] < q[1] for q in queue) :
            queue.append(cur)
        else :
            answer += 1
            if(cur[0] == location) :
                return answer
        print(cur)


print(solution2([2, 1, 3, 2], 2))
print(solution2([1, 1, 9, 1, 1, 1], 0))
