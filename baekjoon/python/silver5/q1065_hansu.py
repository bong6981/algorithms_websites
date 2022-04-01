import sys
input = sys.stdin.readline

def is_hansu(num):
    num = list(str(num))
    if len(num) <= 2:
        return True
    num = [int(n) for n in num]
    gap = num[1] - num[0]
    prev = num[1]
    for n in num[2:]:
        if n - prev != gap:
            return False
        prev = n
    return True

ans = 0
for i in range(1, int(input())+1):
    if is_hansu(i):
        ans+=1
print(ans)






