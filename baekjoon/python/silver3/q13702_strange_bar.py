import sys
input = sys.stdin.readline

N, K = map(int, input().split())
max_q = 2 ** 31 - 1
capacity = [int(input()) for _ in range(N)]
capacity.sort(reverse=True)

end = sum(capacity) // K 
start = 0
ans = 0
while(start <= end):
    mid = (start + end) // 2

    can_divide = 0
    possible = False
    for c in capacity:
        if c < mid :
            break
        if c == mid :
            can_divide += mid
            continue
        
        can_divide += c // K
        if can_divide > mid * K:
            possible = True
            break
    
    if possible:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)


