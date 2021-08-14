def solution(s):
    arr = s.split(" ")
    for i, s in enumerate(arr) :
        word = ''
        for j, c in enumerate(s) :
            if ( j % 2 == 0 ) :
                word += c.upper()
            else :
                word += c.lower()
        arr[i] = word
    print(arr)
    return " ".join(arr)

def solution2(s):
    return " ".join(map(lambda x : "".join(a.lower() if i % 2  else a.upper() for i, a in enumerate(x)), s.split(" ")))

print(solution2('try hello world'))
