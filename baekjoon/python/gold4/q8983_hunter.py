## https://www.acmicpc.net/problem/8983

import sys
input = sys.stdin.readline

def sol_fail():
    m, n, l = map(int, input().split())
    shooting_points = list(map(int, input().split()))
    shooting_points.sort()
    animal_points = []
    for _ in range(n):
        x, y = map(int, input().split())
        if y <= l and (shooting_points[0] - l <= x <= shooting_points[-1]+l):
            animal_points.append((x, y))

    animal_points.sort()
    ans = 0
    idx = 0
    for animal in animal_points:
        start, end = idx, m-1
        while start <= end:
            mid = (start + end) // 2
            if shooting_points[mid] < animal[0]:
                start = mid + 1
            else:
                end = mid - 1
                idx = mid

        if abs(shooting_points[idx] - animal[0]) + animal[1] <= l :
            ans += 1
        elif idx != 0 and abs(shooting_points[idx-1] - animal[0]) + animal[1] <= l :
            ans += 1

    print(ans)


def sol():
    m, n, l = map(int, input().split())
    shooting_points = list(map(int, input().split()))
    shooting_points.sort()
    animal_points = []
    for _ in range(n):
        x, y  = map(int, input().split())
        animal_points.append((x, y))

    ans = 0
    for animal in animal_points:
        if animal[1] > l:
            continue

        start, end = 0, m-1
        point = m
        diff = l + 1

        while start <= end:
            mid = (start + end) // 2
            d = shooting_points[mid] - animal[0]

            if abs(d) < diff:
                diff = abs(d)
                point = mid

            if d < 0:
                start = mid + 1
            else:
                end = mid - 1
        
        if(abs(shooting_points[point] - animal[0]) + animal[1]) <= l:
            ans +=1 
        print(animal, point, ans)

    print(ans)


sol()






