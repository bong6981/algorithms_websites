def solution(enroll, referral, seller, amount):
    
    idx = {}
    for i, p in enumerate(enroll):
        idx[p] = i
    idx["-"] = len(enroll)


    answer = [0] * (len(enroll)+1)    
    for i, s in enumerate(seller):
        sub = s
        money = amount[i] * 100
        while True:
            print(sub, money)
            if sub == "-":
                break
            if int(money * 0.1) < 1:
                answer[idx[sub]] += money
                break
            to_give = int(money * 0.1) 
            answer[idx[sub]] += (money - to_give)
            money = to_give
            sub = referral[idx[sub]]
        print(s, amount[i], answer)
        
    return answer[:-1]

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))
print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["sam", "emily", "jaimie", "edward"], [2, 3, 5, 4]))

