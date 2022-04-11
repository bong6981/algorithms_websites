## https://www.acmicpc.net/problem/10000
import sys
input = sys.stdin.readline

n = int(input())
points = []

## 왼 : -1 
## 오 : 1 
for _ in range(n):
    x, r = map(int, input().split())
    points.append((-1, x-r))
    points.append((1, x+r))

## sort 
## 점의 좌표대로 하되, 같을 때는 오른이 먼저 
points.sort(key=lambda x : (x[1], -x[0]))

stack = []
ans = 1
for point in points:
    if point[0] == -1:
        stack.append(point)
        continue

    width_sum = 0
    while stack:
        prev = stack.pop()
        if prev[0] == 0:
            width_sum += prev[1]
        else:
            width = point[1] - prev[1]
            if width == width_sum:
                ans += 2
            else:
                ans += 1
            stack.append((0, width))
            break

print(ans)
