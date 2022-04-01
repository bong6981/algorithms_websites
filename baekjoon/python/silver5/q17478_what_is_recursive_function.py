import sys
input = sys.stdin.readline

n = int(input())

pre1 = '"재귀함수가 뭔가요?"'
pre2 = '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
pre3 = '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'
pre4 = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
ans = '"재귀함수는 자기 자신을 호출하는 함수라네"'
suf1 = '라고 답변하였지.'
delimeter = '____'

def recursive(i):
    if i == n:
        print(delimeter*n + pre1)
        print(delimeter*n + ans)
        print(delimeter*n + suf1)
        return
    print(delimeter*i + pre1)
    print(delimeter*i + pre2)
    print(delimeter*i + pre3)
    print(delimeter*i + pre4)
    recursive(i+1)
    print(delimeter*i+suf1)


    

print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
recursive(0)
