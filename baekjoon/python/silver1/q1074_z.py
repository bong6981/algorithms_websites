n, r, c = map(int, input().split())

def change(r, c):
    if r == 0:
        if c == 0:
            return 1
        return 2
    else:
        if c == 0:
            return 3
        return 4

def recur(n, r, c):
    # print(n, r, c)
    if n == 1:
        return str(change(r, c))

    pre = str(change(r // (2 ** (n-1)), c // (2 ** (n-1)))-1) 
    # print(pre)
    r += 1
    c += 1
    r %= (2 ** (n-1))
    c %= (2 ** (n-1))
    r -= 1
    c -= 1
    if r == -1 :
        r = 2 ** (n-1) -1
    if c == -1 :
        c = 2 ** (n-1) -1
    return pre + recur(n-1, r, c)
    
def to_decimal(quaternary_number):
    ans = 0
    max_idx = len(quaternary_number) - 1
    for i in range(len(quaternary_number)):
        temp = max_idx - i
        ans += (4 ** temp) * int(quaternary_number[i])
    return ans

# print(recur(n, r, c))
# print(to_decimal(recur(n, r, c))-1)

def sol(n, r, c):
    if n == 0:
        return 0
    half = 2 ** (n-1)
    # 1사분면
    if r < half and c < half :
        return sol(n-1, r, c)
    # 2사분면 
    elif r < half <= c :
        return half ** 2 + sol(n-1, r, c-half)
    elif c < half <= r :
        return 2 * (half ** 2) + sol(n-1, r-half, c) 
    return 3 * (half ** 2) + sol(n-1, r-half, c-half) 

print(sol(n, r, c))
