def solution(s):
    answer =''
    x = 0
    while x < len(s) :
        if s[x] == 'z' :
            answer += '0'
            x += 4
        elif s[x] == 'o' :
            answer += '1'
            x += 3
        elif s[x] == 'e' :
            answer += '8'
            x += 5
        elif s[x] == 'n' :
            answer += '9'
            x += 4
        elif s[x] == 't' :
            if s[x+1] == 'w' :
                answer += '2'
                x += 3 
            else :
                answer += '3'
                x += 5
        elif s[x] == 'f' :
            if s[x+1] == 'o' :
                answer += '4'
                x += 4 
            else :
                answer += '5'
                x += 4  
        elif s[x] == 's' :
            if s[x+1] == 'i' :
                answer += '6'
                x += 3 
            else :
                answer += '7'
                x += 5
        else :
            answer += str(s[x])
            x += 1
    return int(answer)


def solution_2(s):
    num_str = [ 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    answer =''
    for n in num_str :
        s = s.replace(n, str(num_str.index(n)))
    return int(s)

s = "23four5six7"
print(solution_2(s))