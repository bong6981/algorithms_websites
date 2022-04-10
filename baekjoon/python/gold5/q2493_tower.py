## https://www.acmicpc.net/problem/2493
n = int(input())
towers = list(map(int, input().split()))


left_towers = []
for i, v in enumerate(towers, 1):
    if i == 0:
        print(0, end=" ")
        left_towers.append((i, v))
        continue

    while len(left_towers) > 0 :
        if left_towers[-1][1] < v :
            left_towers.pop()
            continue

        if left_towers[-1][1] > v:
            print(left_towers[-1][0], end=" ")
            break
    
    if len(left_towers) == 0:
        print(0, end=" ")
    left_towers.append((i, v))


    


