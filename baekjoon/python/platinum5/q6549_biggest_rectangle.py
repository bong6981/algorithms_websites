import sys
input = sys.stdin.readline

ans = 0

## https://www.acmicpc.net/problem/6549

# 자신이 들어갈 자리 찾는 동시에 그 전것들 pop 해주기 
def add_data(stack, data):
    global ans
    height, now_idx = data
    result_idx = now_idx

    if len(stack) == 0:
        stack.append(data)
        return

    while len(stack) > 0 :
        ele_h, ele_idx = stack[-1]
        if ele_h == height:
            break
   
        if ele_h > height:
            stack.pop()
            area = (now_idx - ele_idx) * ele_h
            result_idx = ele_idx
            ans = max(area, ans)
        else:
            stack.append((height, result_idx))
            break

    if len(stack) == 0:
        stack.append((height, result_idx))
    print(f"result stack : {stack}, ans : {ans}")

while True:
    ans = 0
    numbers = list(map(int, input().split()))
    if len(numbers) == 1:
        break
    n = numbers[0]
    numbers = numbers[1:]

    stack = []
    for i, v in enumerate(numbers):
        add_data(stack, (v, i))
    
    if len(stack) > 0 :
        now_idx = len(numbers)
        for ele in stack:
            h, idx = ele
            ans = max((now_idx - idx) * h, ans)

    print(ans)




