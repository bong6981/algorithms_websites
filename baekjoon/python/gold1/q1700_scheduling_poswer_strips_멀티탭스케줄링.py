#https://www.acmicpc.net/problem/1700

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
used = list(map(int, input().rstrip().split()))

left = N
plugged_in = {}
INF = int(1e9)

cnt = 0
for i in range(K):
    if used[i] in plugged_in:
        continue

    if left <= 0 :
        to_remove = -1
        ans = None
        for p in plugged_in:
            if plugged_in[p] == -1 or plugged_in[p] < i:
                ## 탐색 
                for j in range(i, K):
                    if used[j] == p:
                        plugged_in[p] = j
                        break


            if plugged_in[p] == -1 or plugged_in[p] < i:
                plugged_in[p] = INF
            
            if to_remove < plugged_in[p]:
                to_remove = plugged_in[p]
                ans = p

        
        plugged_in.pop(ans)
        cnt += 1

    plugged_in[used[i]] = -1
    left -= 1
        
print(cnt)



    

    



