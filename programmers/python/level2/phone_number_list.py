def solution(phone_book):
    dic = {}
    dic = {'0':[], '1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[]}

    for num in phone_book :
        dic[num[0]].append(num)
    
    for i in range(10):
        if len(dic[str(i)]) >= 2 :
            dic[str(i)].sort()
            for j in range(len(dic[str(i)])-1) :
                if dic[str(i)][j+1].startswith(dic[str(i)][j]) :
                    return False
    return True

def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    if(len(phoneBook) >= 2) :
        for p1, p2 in zip(phoneBook, phoneBook[1:]):
            if p2.startswith(p1):
                return False
    return True

print(solution(["97674223", "1195524421", "119"]))
print(solution(["1195524421", "97674223", "1"]))
print(solution(["010", "011", "0112", "112"]))




