
def solution(clothes):
    organize = {}
    for item in clothes:
        if(item[1] in organize) :
            organize[item[1]] += 1
        else :
            organize[item[1]] = 2
    
    answer = 1
    for key in organize.keys() :
        answer *= organize[key]

    return answer - 1

def solution2(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    print(cnt.values())
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"], ["crowmask", "face"]]))
print(solution2([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))

