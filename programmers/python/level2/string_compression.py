## 앞에 숫자가 무조건 한자리수라고 생각했는데, a * 10인 경우, 앞의 두글자를 확인해줘야 한다.! 
def solution(s):

    ans_list = []
    for i in range(1, len(s)+1) :
        t = s
        temp = []
        while(len(t) >= i) :
            x = t[0:i]
            t = t[i:len(t)]
            if(len(temp) != 0 and (temp[-1] == x)):
                temp[-2] = str(int(temp[-2]) + 1) 
            else : 
                temp.append('1')
                temp.append(x)

        if(t != '') :
            temp.append(t)

        while('1' in temp):
            temp.remove('1')

        ans_list.append("".join(temp))

    ans_list.sort(key= lambda x : len(x))
    return len(ans_list[0])

def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    print(words)
    print(words[1:] + [''])
    res = []
    cur_word = words[0]
    cur_cnt = 1
    # 아래와 같이 for문을 돌리면 바로 앞과 뒤의 인자들을 비교할 수 있다. 
    for a, b in zip(words, words[1:] + ['']):
        print(a, b)
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1

    print(res)
    # return 해당 문자열의 길이로 해줘서 최종 값에서 min 으로 출력하게 해줌         
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution2(text):
    # 절반을 넘어가면 어쩄든 맨 앞의 문자 + 뒤의 문자니까 전체 문자열 한 것과 똑같다!  
    # 그래서 절반까지의 list를 만들고 거기에 전체 길이를 하나 append 해서 길이에 대한 list를 만든 것 
    # list(range(1, int(len(text)/2) + 1)) + [len(text)]

    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

# print(solution("aaaaaaaaaaaaaaa"))
print(solution2("aabbaccc"))
# print(solution("ababcdcdababcdcd"))
# print(solution("abcabcdede"))
# print(solution("abcabcabcabcdededededede"))
# print(solution("xababcdcdababcdcd"))





