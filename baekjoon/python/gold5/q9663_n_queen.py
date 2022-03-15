## https://www.acmicpc.net/problem/9663
n = int(input())
ans = 0
positions = []

def is_possible_to_attack(r1, c1, r2, c2):
    if c1 == c2:
        return True
    if r1 + c1 == r2 + c2:
        return True
    if r1 - c1 == r2 - c2:
        return True
    return False

def sol(row):
    global ans
    global positions
    if row == n :
        ans += 1
        return
    
    for col in range(n):
        possible = True
        for i, p in enumerate(positions):
            if is_possible_to_attack(i, p, row, col):
                possible = False
                break
        if possible:
            positions.append(col)
            sol(row+1)
            positions.pop()

sol(0)
print(ans)

