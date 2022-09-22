import sys 
input = sys.stdin.readline 

t = int(input())
ns = []
for i in range(t):
    ns.append(int(input()))

v = max(ns)
ans = [0] * (v+1)
ans[1] = 1
ans[2] = 2
ans[3] = 4
for i in range(4, v+1):
    ans[i] += (ans[i-3] + ans[i-2] + ans[i-1])

for n in ns:
    print(ans[n])

