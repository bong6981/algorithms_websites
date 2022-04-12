# https://www.acmicpc.net/problem/2261
import sys 
input = sys.stdin.readline

n = int(input().rstrip())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

points.sort()

def get_dis(p1, p2):
    return (p1[0] - p2[0]) **2 + (p1[1] - p2[1]) **2

def check_dis_all(start, end):
    ans = 1e9
    for i in range(start, end):
        for j in range(i+1, end+1):
            ans = min(ans, get_dis(points[i], points[j]))
    return ans

def cross_dis(start, mid, end, min_dis):
    cands = []
    for i in range(start, end+1):
        dis = points[i][0] - points[mid][0]
        if(dis ** 2 < min_dis):
            cands.append(points[i])
    
    cands.sort(key=lambda x : x[1])

    for i in range(len(cands)-1):
        for j in range(i+1, len(cands)):
            dis = cands[j][1] - cands[i][1]
            if  dis ** 2 < min_dis:
                min_dis = min(get_dis(cands[i], cands[j]), min_dis)
            else:
                break
    return min_dis

def find_min(start, end):
    if end - start + 1 < 4:
        return check_dis_all(start, end)

    mid = (start + end) // 2
    ans = min(find_min(start, mid), find_min(mid+1, end))
    ans = min(ans, cross_dis(start, mid, end, ans))
    return ans

print(find_min(0, len(points)-1))



