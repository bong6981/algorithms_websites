## https://www.acmicpc.net/problem/1541
import sys
input = sys.stdin.readline

expression = input().rstrip().split('-')

first = sum(list(map(int, expression[0].split("+"))))
for n in expression[1:]:
    first -= sum(list(map(int, n.split("+"))))

print(first)
    


    
