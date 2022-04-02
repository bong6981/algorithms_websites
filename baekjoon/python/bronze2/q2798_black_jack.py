import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort()

answer = []
for i, num in enumerate(cards):
    if num > m:
        break
    acc = num
    for j in range(i+1, len(cards)):
        j_val = cards[j]
        if acc + j_val > m:
            break
        second_acc = acc + j_val
        for k in range(j+1, len(cards)):
            k_val = cards[k]
            if acc + k_val > m :
                break
            last_acc = second_acc + k_val
            if last_acc <= m :
                answer.append(last_acc)

answer.sort(reverse=True)
print(answer[0])



