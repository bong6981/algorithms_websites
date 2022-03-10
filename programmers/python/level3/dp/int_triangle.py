# https://programmers.co.kr/learn/courses/30/lessons/43105
def solution(triangle):
    prev = triangle[0]
    for t in triangle[1:]:
        for i in range(len(t)):
            if i == 0:
                t[i] += prev[0]
                continue
            if i == len(t) - 1:
                t[i] += prev[i-1]
                continue
            t[i] += max(prev[i-1], prev[i])
        prev = t
    return max(prev)


print(solution([[0]]))
print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
