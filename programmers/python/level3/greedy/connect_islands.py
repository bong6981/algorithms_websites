# https://programmers.co.kr/learn/courses/30/lessons/42861?language=python3
def find_p(c):
    if parent[c] != c:
        parent[c] = find_p(parent[c])
    return parent[c]

def union(x, y):
    x = find_p(x)
    y = find_p(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y    

def solution(n, costs):
    #섬번호가 순서대로 주어진다고 가정 0 ~ n-1
    global parent
    parent = [0] * (n)
    edges = []

    for i in range(n):
        parent[i] = i
    
    for cost in costs:
        x, y, c = cost
        edges.append((c, x, y))

    edges.sort()

    result = 0

    for edge in edges:
        c, x, y = edge
        if find_p(x) != find_p(y) :
            union(x, y)
            result += c

    return result

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
