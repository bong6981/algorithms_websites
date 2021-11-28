# https://programmers.co.kr/learn/courses/30/lessons/17680?language=python3
# 카카오 블라인드 1차
def solution(cacheSize, cities):
    time = 0
    cache = []
    if cacheSize == 0:
        return len(cities) * 5
    for c in cities:
        # 캐시에 있는지 확인
        c = c.lower()
        if c in cache:
            ## idex로 접근 검색
            cache.remove(c)
            time += 1
            cache.append(c)
            # print(c, time)
            continue
        time += 5
        if len(cache) == cacheSize:
            cache.pop(0)
            cache.append(c)
            continue
        cache.append(c)
        # print(c, time)
    return time


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))


## deque의 maxlen을 활용하면 더 편리하다. 
def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time
