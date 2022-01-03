# https://www.acmicpc.net/problem/2798
def solution():
    n, m = map(int, input().split())
    cards = list(map(int, input().split()))
    cards.sort()

    answer = 0
    for i in range(0, n-2):
        x = cards[i]
        if x >= m :
            break
        for j in range(i+1, n-1):
            y = x + cards[j]
            if y >= m :
                break
            for k in range(j+1, n):
                z = y + cards[k]
                if z > m:
                    break
                answer = max(answer, z)

    return answer

print(solution())
