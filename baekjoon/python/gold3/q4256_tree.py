## https://www.acmicpc.net/problem/4256
from collections import deque
import sys
input = sys.stdin.readline


T = int(input().rstrip())


def find(start, end):
    if len(preorder) == 0:
        return
        
    if start > end :
        return
    
    last = preorder.popleft()
    if start == end:
        ans.append(inorder[start])
        return
    
    ## start ~ last -1 / last / last + 1 ~ end 
    mid = inorder.index(last)
    find(start, mid-1)
    find(mid+1, end)
    ans.append(inorder[mid])
    

for _ in range(T):
    ans = []
    N = int(input().rstrip())
    preorder = deque(map(int, input().rstrip().split()))
    inorder = list(map(int, input().rstrip().split()))

    idx = 0
    find(0, N-1)
    print(*ans)


