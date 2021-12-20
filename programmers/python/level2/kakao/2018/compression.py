import string
from collections import deque

def solution(msg):
    dic = {}
    chars = list(string.ascii_uppercase)
    for i, c in enumerate(chars) :
        dic[c] = i + 1
    last = 26

    msg = deque(msg)
    answer = []
    while(msg):
        ## 사전에 있는 가장 긴 문자열 찾기 
        now = ''
        temp = ''
        while True:
            now += msg.popleft()
            if not msg:
                break
            temp = now + msg[0]
            if not temp in dic :
                break
        answer.append(dic[now])
        last += 1
        if temp != '':
            dic[temp] = last
    return answer

# print(solution("KAKAO"))
# print(solution("TOBEORNOTTOBEORTOBEORNOT"))
# print(solution("ABABABABABABABAB"))


