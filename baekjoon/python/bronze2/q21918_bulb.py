import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
now = [0]
now.extend(list(map(int,input().rstrip().split())))

for _ in range(m):
    op, x, y = map(int, input().split())
    if op == 1:
        now[x] = y
    elif op == 2:
        for i in range(x, y+1):
            if now[i] == 1:
                now[i] = 0
            else:
                now[i] = 1
    elif op == 3:
        for i in range(x, y+1):
            now[i] = 0
    else:
        for i in range(x, y+1):
            now[i] = 1

print(*now[1:])


