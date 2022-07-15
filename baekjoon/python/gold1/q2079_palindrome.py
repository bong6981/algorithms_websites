
given = input()
N = len(given)
dp = [[-1] * (N) for _ in range(N)]

for i in range(N):
    dp[i][i] = 1


def is_pal(s, e):
    if dp[s][e] != -1:
        return dp[s][e]
    
    if s[s] != s[e]:
        dp[s][e] = 0
        return False
    
    if s == e or e == s + 1 :
        return True

    return is_pal(s+1, e-1)
