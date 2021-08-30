from collections import deque

def solution(bridge_length, weight, truck_weights):
    trucks = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    weight_bridge = 0
    time = 0

    while True :
        weight_bridge -= bridge.popleft()
        bridge.append(0)
        if(trucks != deque([]) and weight_bridge + trucks[0] <= weight) :
            new = trucks.popleft()
            bridge.pop()
            bridge.append(new)
            weight_bridge += new 

        time += 1
        ## 조건문 순서 바꿔주면 fail 된다. [0] * bridege_length를 확인하는 부분이 오래 걸리나봄 
        if(trucks == deque([]) and bridge == deque([0] * bridge_length)) :
            break
    return time

## while 문을 truck이 비었을 때로 설정하고 마지막에 그 브릿지만큼 더해준 것이 똑띠, reverse 써서 queue 안만들어도 된 것 똑띠 
def solution2(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    total_weight = 0
    step = 0
    truck_weights.reverse()

    while truck_weights:
        total_weight -= bridge.popleft()
        if total_weight + truck_weights[-1] > weight:
            bridge.append(0)
        else:
            truck = truck_weights.pop()
            bridge.append(truck)
            total_weight += truck
        step += 1

    step += bridge_length

    return step


print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))


