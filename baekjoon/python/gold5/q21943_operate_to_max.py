
## https://www.acmicpc.net/source/40879427
def pypy_sol():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(100000)

    def pick(idx, arr):
        global ans
        if idx == len(numbers):
            ans = max(ans, cal(arr))
            return

        for i in range(len(arr)):
            arr[i] += numbers[idx] 
            pick(idx+1, arr)
            arr[i] -= numbers[idx]

    def cal(arr):
        ans = 1
        for e in arr:
            ans *= e
        return ans

    n = int(input())
    numbers = list(map(int, input().split()))
    cnt_add, cnt_mul = map(int, input().split())
    cnt = cnt_mul+1
    ans = 0
    pick(0, [0 for _ in range(cnt)])
    print(ans)


