import sys
input = sys.stdin.readline

def binary_search(less_than, end):
    start = 0
    ans = -1
    while start <= end:
        mid = (start + end) // 2
        if b[mid] >= less_than:
            end = mid - 1
        else:
            ans = mid
            start = mid + 1
    return ans

for _ in range (int(input())) : 
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort(reverse=True)
    b.sort()

    ans = 0
    last = len(b)-1
    for e in a :
        last = binary_search(e, last)
        if last == -1 :
            break
        ans += last + 1
    print(ans)
        




            
        





