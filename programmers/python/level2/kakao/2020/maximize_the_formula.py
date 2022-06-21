# https://programmers.co.kr/learn/courses/30/lessons/67257?language=python3
from itertools import permutations
import copy
def solution(expression):
    new_expression = []
    operation_info = {}
    num = ""
    operations = ["+", "-", "*"]
 
    
    for op in operations:
        operation_info[op] = []

    for c in expression:
        if c.isdigit() :
            num += c
        else:
            new_expression.append(int(num))
            new_expression.append(c)
            num = ""
            operation_info[c].append(len(new_expression)-1)

    new_expression.append(int(num))
    expression = new_expression
    
    included_operations = []
    for op in operations:
        if operation_info[op] == []:
            continue
        included_operations.append(op)
        operation_info[op].sort()

    answer = 0
    for p in permutations(included_operations, len(included_operations)):
        temp_expression = copy.deepcopy(expression)
        for op in list(p):
            for idx in operation_info[op]:
                for i in range(idx-1, -1, -1):
                    if temp_expression[i] != "":
                        prev_idx = i
                        break
                for i in range(idx+1, len(temp_expression)):
                    if temp_expression[i] != "":
                        next_idx = i
                        break
                if op == "+":
                    temp_expression[prev_idx] += temp_expression[next_idx]
                elif op == "-":
                    temp_expression[prev_idx] -= temp_expression[next_idx]
                else:
                    temp_expression[prev_idx] *= temp_expression[next_idx]
                temp_expression[idx] = ""
                temp_expression[next_idx] = ""
        answer = max(answer, abs(temp_expression[0]))
    return answer

from collections import defaultdict
from itertools import permutations

# 0621 다시 풀었을 때 풀이 
def solution2(expression):
    exp = list(expression)
    
    info = defaultdict(list)
    
    ops = ['+', '-', '*']
    used_ops = set()
    start = 0
    idx = 0
    new_exp = []

    while idx < len(exp):
        if exp[idx] in ops:
            new_exp.append(''.join(exp[start:idx]))
            start = idx + 1
            used_ops.add(exp[idx])
            info[exp[idx]].append(len(new_exp))
            new_exp.append(exp[idx])
        if idx == len(exp) -1 :
            new_exp.append((''.join(exp[start:idx+1])))

        idx += 1
    exp = new_exp
    print(new_exp)
    print(info)
    ans = 0
    ## 가능한 우선순위 순서  
    for p in permutations(list(used_ops)):
        order = list(p)
        tmp_exp = exp[::]
        print("====", order)
        for op in order:
            for idx in info[op]:
                ##find_prev
                prev = idx -1 
                prev_num =0
                while(prev >= 0):
                    if tmp_exp[prev] == '#':
                        prev -= 1
                    else:
                        prev_num = int(tmp_exp[prev])
                        break
                ##find_next
                next_ = idx + 1 
                next_num = 0
                while next_ < len(exp):
                    if tmp_exp[next_] == '#':
                        next_ += 1
                    else:
                        next_num = int(tmp_exp[next_])
                        break
                num = 0
                if op == '+':
                    num = prev_num + next_num
                elif op == '-':
                    num = prev_num - next_num
                elif op == '*':
                    num = prev_num * next_num

                for i in range(prev, next_ + 1):
                    tmp_exp[i] = '#'
                tmp_exp[idx] = str(num)
                print(tmp_exp)
        for e in tmp_exp:
            if e != "#":
                print(int(e))
                ans = max(ans, abs(int(e)))
        
    return ans


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
# ## 프로그래머스 다른 사람의 풀이1
# def solution(expression):
#     operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
#     answer = []
#     for op in operations:
#         a = op[0]
#         b = op[1]
#         temp_list = []
#         for e in expression.split(a):
#             print("a: ", a)
#             print(e.split(b))
#             temp = [f"({i})" for i in e.split(b)]
#             print("b ", b)
#             print(temp)
#             print(b.join(temp))
#             temp_list.append(f'({b.join(temp)})')
#         print(a.join(temp_list))
#         answer.append(abs(eval(a.join(temp_list))))
#     return max(answer)
# print(solution("100-200*300-500+20"))
# print(solution("50*6-3*2"))

# ## 프로그래머스 다른 사람의 풀이2
# def solution(expression):
#     operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
#     answer = []
#     for op in operations:
#         a = op[0]
#         b = op[1]
#         temp_list = []
#         for e in expression.split(a):
#             print("a: ", a)
#             print(e.split(b))
#             temp = [f"({i})" for i in e.split(b)]
#             print("b ", b)
#             print(temp)
#             print(b.join(temp))
#             temp_list.append(f'({b.join(temp)})')
#         print(a.join(temp_list))
#         answer.append(abs(eval(a.join(temp_list))))
#     return max(answer)
print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))

