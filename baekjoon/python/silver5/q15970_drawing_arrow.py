## https://www.acmicpc.net/problem/15970
import sys
input = sys.stdin.readline
n = int(input())
color = [-1 for _ in range(n+1)]
points = []
for _ in range(n):
    p, c = map(int, input().split())
    points.append((p, c))

max_point = 10 ** 5
sorted_points= sorted(points, key=lambda x: x[0])

answer = [0 for _ in range(max_point)]
for point in sorted_points:
    p, c = point
    if color[c] != -1:
        answer[p] = p - color[c]
    color[c] = p

color = [-1 for _ in range(n+1)]
for i in range(len(sorted_points)-1, -1, -1):
    p, c = sorted_points[i]
    if color[c] != -1:
        if answer[p] == 0 or answer[p] > color[c] - p:
            answer[p] = color[c] - p
    color[c] = p


print(sum(answer))
