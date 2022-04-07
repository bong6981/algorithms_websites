from operator import le
import sys
input = sys.stdin.readline

def is_vps(bracket_str):
    cnt = 0
    for c in bracket_str:
        if c == "(":
            cnt += 1
        else:
            cnt -=1

        if cnt < 0:
            return False

    if cnt != 0:
        return False
    return True

#08:30
n = int(input())
for _ in range(n):
    if is_vps(input().rstrip()):
        print("YES")
        continue
    print("NO")


        
