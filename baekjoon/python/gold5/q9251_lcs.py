# https://www.acmicpc.net/problem/9251
import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

str1 = '0' + input().rstrip()
str2 = '0' + input().rstrip()
graph = [[0] * (len(str1)) for _ in range(len(str2))]

for i in range(1, len(str2)):
    for j in range(1, len(str1)):
        if str2[i] == str1[j]:
            graph[i][j] = graph[i-1][j-1] + 1
        else:
            graph[i][j] = max(graph[i][j-1], graph[i-1][j])

print(graph[len(str2)-1][len(str1)-1])
