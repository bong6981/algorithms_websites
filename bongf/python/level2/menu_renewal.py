from itertools import combinations
def solution(orders, course):
    temp = [{} for _ in range(len(course))]
    for i, c in enumerate(course) :
        for o in orders:
            if(len(o) < c):
                continue
            else :
                for x in combinations(o, c):
                    x = tuple(sorted(x, key = lambda x: x))
                    if x in temp[i]:
                        temp[i][x] += 1 
                    else:
                        temp[i][x] = 1

    answer = []         
    for t in temp :
        small_answer = []
        max_value = 2
        for y in t:
            if(t[y] > max_value) :
                max_value = t[y]
                small_answer = []
                small_answer.append(y)
            elif t[y] == max_value :
                small_answer.append(y)
        answer.extend(small_answer)
    real_answer = []
    for x in answer : 
        x = "".join(x)
        real_answer.append(x)
    return sorted(real_answer)


import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_comb = []
        for order in orders:
            # 여기서 sorted(order)를 넣어주지 않으면 w, x / x ,w  이렇게 순서 없이 들어가서 나중에 계산할 때 서로 다른 2개로 취급 
            order_comb += itertools.combinations(sorted(order), course_size)
        
        most_ordered = collections.Counter(order_comb).most_common()
        result += [ k for k,v in most_ordered if v > 1 and v == most_ordered[0][1]]
    return [''.join(v) for v in sorted(result)]

# print(solution2(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution2(["XYZ", "XWY", "WXA"], [2,3,4]))
