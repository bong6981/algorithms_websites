#https://programmers.co.kr/learn/courses/30/lessons/64065
def solution(s):
    s = s[2:-2].split("},{")
    tuple = []
    for c in s :
        tuple.append(list(map(int, c.split(","))))

    tuple.sort(key = lambda x: len(x))
    answer = []
    for t in tuple:
        if len(t) == 1:
            answer.append(int(t[0]))
        else:
            for x in t :
                x  = int(x)
                if x not in answer:
                    answer.append(x)
    return answer

from collections import deque
def solution_old(s):
    s = deque(s[1:-1])

    input_list = []
    while s:
        x = s.popleft()
        if x=='{' :
            str_tem = ''
            while True:
                y = s.popleft()
                if y == '}':
                    break
                str_tem += y
            input_list.append(set(map(int, str_tem.split(","))))
    input_list.sort(key=lambda x: len(x))
    answer = []
    now = set()
    for s in input_list:
        left = s - now
        answer.append(*left)
        now = s
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))


def other(s):
    answer = []
    s1 = s.lstrip('{').rstrip('}').split('},{')
    new_s = []
    for i in s1:
        new_s.append(i.split(','))
    new_s.sort(key = len)
    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))
    return answer

print(other("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
