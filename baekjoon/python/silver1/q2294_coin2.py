import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, K = map(int, input().split())
coins = [int(input().rstrip()) for _ in range(N)] ## input
coins.sort()
MAX = 100001
coin_cnt = [MAX] * (MAX)
def cal(amount):
    if coin_cnt[amount] != MAX:
        return coin_cnt[amount]

    if amount == 0:
        return 0
    
    if amount < coins[0]:
        return -1

    result = MAX
    for c in coins:
        ret = cal(amount-c)
        if ret == -1:
            continue
        result = min(result, ret + 1)

    if result == MAX:
        coin_cnt[amount] = -1
    else:
        coin_cnt[amount] = min(coin_cnt[amount], result)
    return coin_cnt[amount]

print(cal(K))

