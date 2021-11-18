## https://programmers.co.kr/learn/courses/30/lessons/72412
from itertools import combinations
from bisect import bisect_left
def solution(info, query):
    db = {}
    for data in info:
        data = data.split()
        score = int(data[-1])
        data = data[:-1]
        for n in range(5):
            coms = list(combinations(range(4), n))
            for c in coms :
                temp = data.copy()
                for i in c :
                    temp[i] = '-'
                temp = ' '.join(temp)
                if temp in db:
                    db[temp].append(score)
                else:
                    db[temp] = [score]
    
    for v in db.values():
        v.sort()

    answer = []
    for q in query :
        q = [ i for i in q.split() if i != 'and']
        q_condition = ' '.join(q[:-1])
        q_score = int(q[-1])
        if q_condition in db : 
            data = db[q_condition]
            if len(data) > 0 :
                # answer.append(len(data) - bisect_left(data, q_score))
                ## 통과는 하는데 bisect보다 느리다 
                start, end = 0, len(data)
                while start < end:
                    mid = (start + end) // 2
                    if(data[mid] >=q_score) :
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(data) - end)
        else:
            answer.append(0)
    return answer
  
def solution2(info, query):
    data = dict()
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a, b, c, d), list())
    
    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[(a, b, c, d)].append(int(i[4]))

    for k in data:
        data[k].sort()

        # print(k, data[k])

    answer = list()
    for q in query:
        q = q.split()

        pool = data[(q[0], q[2], q[4], q[6])]
        find = int(q[7])
        l = 0
        r = len(pool)
        mid = 0
        while l < r:
            mid = (r+l)//2
            if pool[mid] >= find:
                r = mid
            else:
                l = mid+1
            # print(l, r, mid, answer)
        # answer.append((pool, find, mid))
        answer.append(len(pool)-l)

    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution2(info, query))



