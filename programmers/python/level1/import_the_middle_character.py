def solution(s):
    t = len(s) - 1
    if t % 2 != 0 :
        return  s[int(len(s)/2-1)] + s[int(len(s)/2)]
    return s[int(t / 2)]

s = "abcd"
print(solution(s))