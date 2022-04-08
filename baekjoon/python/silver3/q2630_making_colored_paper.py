from collections import deque
## https://www.acmicpc.net/problem/2630
def sol(paper):
    global white, blue
    papers = deque([paper])
    while len(papers) > 0:
        paper = papers.pop()
        rs, re, cs, ce = paper
        len_paper = re - rs + 1
        is_same_color, total = check(paper)
        if is_same_color:
            if total == 0:
                white += 1
            else:
                blue += 1
        else:
            if len_paper == 2:
                blue += total
                white += (4 - total)
            else:
                middle_r = (re + rs) // 2
                middle_c = (ce + cs) // 2 
                papers.append([rs, middle_r, cs, middle_c])
                papers.append([rs, middle_r, middle_c+1, ce])
                papers.append([middle_r+1, re, cs, middle_c])
                papers.append([middle_r+1, re, middle_c+1, ce])

def check(paper):
    rs, re, cs, ce = paper
    l = re - rs + 1
    expected_sum = l * l 

    total = 0
    for i in range(rs, re+1):
        total += sum(whole_paper[i][cs:ce+1])

    if total == expected_sum or total == 0:
        return True, total
    return False, total

whole_paper = []
n = int(input())
for _ in range(n):
    whole_paper.append(list(map(int, input().split())))

white = 0
blue = 0
sol([0, n-1, 0, n-1])

print(white)
print(blue)
