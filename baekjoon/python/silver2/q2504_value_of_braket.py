import sys
sys = sys.stdin.readline


def sol():
    bracket_str = input()
    stack = []
    acc = [0] * 30
    for c in bracket_str:
        if c == "(" or c == "[":
            stack.append(c)
        elif c == ")" :
            if len(stack) > 0 and stack[-1] == "(" :
                stack.pop()
                previos_score = acc[len(stack)+1]
                acc[len(stack)+1] = 0
                if previos_score == 0:
                    previos_score = 1
                acc[len(stack)] += 2 * previos_score 
            else:
                return 0
        elif c == "]" :
            if len(stack) > 0 and stack[-1] == "[" :
                stack.pop()
                previos_score = acc[len(stack)+1]
                acc[len(stack)+1] = 0
                if previos_score == 0:
                    previos_score = 1
                acc[len(stack)] += 3 * previos_score 
            else:
                return 0
    return acc[0]

print(sol())

    
