from collections import Counter

def solution(str1, str2):
    str1_list = []
    str2_list = []
    for i in range(len(str1)-1):
        s = str1[i:i+2]
        if s.isalpha():
            str1_list.append(s.lower())

    for i in range(len(str2)-1):
        s = str2[i:i+2]
        if s.isalpha():
            str2_list.append(s.lower())

    total = len(str1_list) + len(str2_list)
    bunza = 0
    if total == 0 :
        return 65536

    str1_list.sort()
    str2_list.sort()
    s2idx = 0 
    for i in range(len(str1_list)):
        s = str1_list[i]
        for j in range(s2idx, len(str2_list)):
            if s == str2_list[j]:
                s2idx = j+1
                bunza += 1
                total -= 1
                break
        if s2idx == len(str2_list):
            break
    return int(bunza/total * 65536)

def solution_old(str1, str2):
    st1 = []
    for i in range(len(str1)):
        if i == len(str1) - 1 :
            break
        c1 = str1[i]
        c2 = str1[i+1]
        if c1.isalpha() and c2.isalpha() :
            if c1.isupper():
                c1 = c1.lower()
            if c2.isupper():
                c2 = c2.lower()
            st1.append(c1+c2)
    
    st2 = []
    for i in range(len(str2)):
        if i == len(str2) - 1 :
            break
        c1 = str2[i]
        c2 = str2[i+1]
        if c1.isalpha() and c2.isalpha() :
            if c1.isupper():
                c1 = c1.lower()
            if c2.isupper():
                c2 = c2.lower()
            st2.append(c1+c2)

    st1_counter = Counter(st1)
    st2_counter = Counter(st2)

    bunza = 0
    bunmo = 0 
    for c1 in st1_counter:
        if c1 in st2_counter: 
            bunza += min(st1_counter[c1], st2_counter[c1])
            bunmo += max(st1_counter[c1], st2_counter[c1])
        else:
            bunmo += st1_counter[c1]
    
    for c2 in st2_counter:
        if not c2 in st1_counter:
            bunmo += st2_counter[c2]

    if bunmo == 0:
        return 65536
    return int(bunza / bunmo * 65536)

print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))

print("aA".isalpha()) ##True

def solution2(str1, str2):
    str1 = [str1[n:n+2].lower() for n in range(len(str1)-1) if str1[n:n+2].isalpha()]
    str2 = [str2[n:n+2].lower() for n in range(len(str2)-1) if str2[n:n+2].isalpha()]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return int((gyo_sum/hap_sum)*65536)
