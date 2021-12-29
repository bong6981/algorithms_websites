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

print(solution())
