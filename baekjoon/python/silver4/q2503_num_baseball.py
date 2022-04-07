# 동일자리 위치 -> 스트라이크
# 숫자가 있긴 하나 다른 위치 -> 볼

from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
hints = []
for _ in range(n):
    hints.append(list(map(int, input().split())))

nums = list(range(1, 10))
cand_nums = [list(can) for can in permutations(nums, 3)]


def is_answer(hint, ans):
    num, strike, ball = hint
    num = str(num)

    ans_strike = 0
    ans_ball = 0

    for i in range(3):
        num_element = int(num[i])
        if num_element == ans[i]:
            ans_strike += 1
        elif num_element in ans:
            ans_ball += 1

    if strike == ans_strike and ball == ans_ball:
        return True

    return False


ans = 0
for cand in cand_nums:
    right = True
    for hint in hints:
        if not is_answer(hint, cand):
            right = False
            break
    if right:
        ans += 1
print(ans)
