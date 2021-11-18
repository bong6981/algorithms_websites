def solution(s, n):
    answer = ''
    for c in s :
        if c != " " :
            ascii_n = ord(c)
            if 65 <= ascii_n <= 90 :
                ascii_n += n 
                if ascii_n > 90 :
                    ascii_n -= 26
            else :
                ascii_n += n 
                if ascii_n > 122 : 
                    ascii_n -= 26
            c = chr(ascii_n)
        answer += c
    return answer

def solution2(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)

s = "Z"
print(solution2(s, 1))