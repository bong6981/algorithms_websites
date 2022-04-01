from re import S


t = int(input())
for _ in range(t):
    score = 0
    acc_score = 0
    for e in list(input()) :
        if e == 'O':
            if acc_score != 0:
                acc_score += 1
            else:
                score += sum(v for v in range(1, acc_score+1))
                acc_score = 1
        else:
            score += sum(v for v in range(1, acc_score+1))
            acc_score = 0
    if acc_score != 0:
        score += sum(v for v in range(1, acc_score+1))
    print(score)        

