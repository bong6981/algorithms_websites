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


visited_c = [False for _ in range(n)]
visited_r_up = [False for _ in range((n-1) * 2 + 2)]
visited_l_up = [False for _ in range((n-1) * 2 + 2)]
cnt = 0

def recur(i):
    global cnt
    if i == n :
        cnt += 1
        return

    for j in range(n):
        r_up_idx = i + j
        l_up_idx = i - j
        if l_up_idx < 0:
            l_up_idx += 2 * n
        if (not visited_c[j]) and (not visited_l_up[l_up_idx]) and (not visited_r_up[r_up_idx]):
            visited_c[j] = True
            visited_l_up[l_up_idx] = True
            visited_r_up[r_up_idx ] = True
            recur(i+1)
            visited_c[j] = False
            visited_l_up[l_up_idx] = False
            visited_r_up[r_up_idx ] = False

recur(0)
print(cnt)
