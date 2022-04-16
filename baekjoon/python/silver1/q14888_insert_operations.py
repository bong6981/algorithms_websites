## https://www.acmicpc.net/problem/14888

n = int(input())
numbers = list(map(int, input().split()))
pl, mi, mul, div = map(int, input().split())
left = pl + mi + mul+ div
left_operations = [pl, mi, mul, div]
operations = []
max_val = ''
min_val = ''

def recurFuc(left):
    global max_val
    global min_val
    if left == 0 :
        result = cal()
        if max_val == '':
            max_val = result
            min_val = result
        else:
            max_val = max(max_val, result)
            min_val = min(min_val, result)
        return
    
    for i in range(4):
        if left_operations[i] > 0:
            left -= 1
            operations.append(i)
            left_operations[i] -= 1
            recurFuc(left)
            left +=1
            operations.pop()
            2
            left_operations[i] += 1


def cal():
    num = numbers[0]
    for i, v in enumerate(numbers[1:]):
        op = operations[i-1]
        if op == 0 :
            num += v
        elif op == 1 :
            num -= v
        elif op == 2:
            num *= v
        else:
            if num < 0 and v > 0 :
                num = -num
                num //= v
                num = -num
            else:
                num //= v
    return num

recurFuc(left)
print(max_val)
print(min_val)

### 0416 update 
import sys
input = sys.stdin.readline

N = (int)(input().rstrip())
numbers = list(map(int, input().rstrip().split()))
# 덧, 뺄, 곱, 나
op_cnt = list(map(int, input().rstrip().split()))

ans_max = -1e9
ans_min = 1e9

def sol(idx, number):
    global op_cnt, ans_min, ans_max
    if idx == N:
        ans_max = max(ans_max, number)
        ans_min = min(ans_min, number)
    for i, v in enumerate(op_cnt):
        if v > 0:
            if i == 0:
                op_cnt[0] -= 1
                sol(idx+1, number + numbers[idx])
                op_cnt[0] += 1
            elif i == 1:
                op_cnt[1] -= 1
                sol(idx+1, number - numbers[idx])
                op_cnt[1] += 1
            elif i == 2:
                op_cnt[2] -= 1
                sol(idx+1, number * numbers[idx])
                op_cnt[2] += 1
            else:
                if number < 0:
                    temp = - ((-number) // numbers[idx])
                else:
                    temp = number // numbers[idx]
                op_cnt[3] -= 1
                sol(idx+1, temp)
                op_cnt[3] += 1

sol(1, numbers[0])
print(ans_max)
print(ans_min)


