# https://www.acmicpc.net/problem/2805
def solution():
    n, m = map(int, input().split())
    trees = list(map(int, input().split()))
    trees.sort(reverse=True)
    start = 0
    end = trees[0]
    answer = 0
    while start <= end :
        total = 0
        mid = (start + end) // 2
        for tree in trees :
            if tree <= mid :
                break
            total += tree - mid
        if total < m :
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
    return answer

# print(solution())

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

def find_height():
    start = 0
    end = max(trees)
    ans = -1

    while start <= end:
        mid = (start + end) // 2
        to_get = 0
        for tree in trees:
            left = tree - mid
            if left < 0:
                left = 0
            to_get += left
        
        if to_get >= m :
            ans = mid
            start = mid + 1
        else:
            end = mid -1
    
    return ans

print(find_height())           



