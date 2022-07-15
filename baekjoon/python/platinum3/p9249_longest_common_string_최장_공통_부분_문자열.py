import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()

def sol_fail():
    from collections import defaultdict

    B_dix = defaultdict(list)

    for i, c in enumerate(B):
        B_dix[c].append(i)

    ans_cnt = 0
    ans = None
    for i, c in enumerate(A):
        if c not in B_dix:
            continue
        
        for j in B_dix[c]:
            cnt = 1
            j += 1
            if j == len(B):
                break
            for k in range(i+1, len(A)):
                if j == len(B):
                    break

                if A[k] == B[j]:
                    cnt += 1
                    j += 1
                else:
                    break
            ans_cnt = max(ans_cnt, cnt)
            if ans_cnt == cnt:
                ans = (i, i+cnt)

    print(ans_cnt)
    print(A[ans[0]:ans[1]])


def sol_dp():
    dp = [[0] * (len(B)+1) for _ in range(len(A)+1)]
    ans_string = [[''] * (len(B)+1) for _ in range(len(A)+1)]
    ans = 0
    ans_idx = (0, 0)
    
    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                ans_string[i][j] = ans_string[i-1][j-1] + A[i-1]
                ans = max(ans, dp[i][j])
                if ans == dp[i][j]:
                    ans_idx = (i, j)
            else:
                dp[i][j] = 0
    print(ans)
    print(ans_string[ans_idx[0]][ans_idx[1]])

sol_dp()
