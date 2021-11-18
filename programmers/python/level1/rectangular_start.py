a, b = map(int, input().split(' '))
for __ in range(b): 
    print(a * '*' )

## for문 안돌리고 그냥 곱하기로 
def solution2():
    a, b = map(int, input().strip().split(' '))
    answer = ('*'*a +'\n')*b
    print(answer)
