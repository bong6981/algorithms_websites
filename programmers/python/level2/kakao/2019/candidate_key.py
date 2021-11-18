from itertools import combinations

## 일단 tuple의 원소들이 들어오는 순서가 같다고 가정 
## solution2보다 빠르다 
def solution(relation):
    x = len(relation)
    n = len(relation[0])
    candidates = []
    # print(n)
    for i in range(1, n+1):
        for c in combinations(range(0, n), i):
            candidates.append(list(c))
    
    cnt = 0
    print(candidates)
    for now, idxs in enumerate(candidates) :
        if(idxs == []):
            continue
        idxs = sorted(idxs)
        s1 = set()
        for r in relation:
            s2 = []
            for i in idxs:
                s2.append(r[i])
            s2 = tuple(s2)
            if s2 in s1 :
                break
            s1.add(s2)
        

        if(len(s1) < x):
            continue
        cnt += 1
        for a in range(now+1, len(candidates)):
            contain = True
            for b in idxs:
                if(b not in candidates[a]):
                    contain = False
                    break
            if contain :
                candidates[a] = []
     
    return cnt

## 4 = len(relation[0])
## 6 = len(relation)
# relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
# i = 1, 10, 11, 100, 101, 110, 111, 1000, 1001, ... 1100, 1101, 1110, 1111
# for i in range(1, 1<<4):
#     # print(f'i는 {i}')    
#     # print(bin(i))
#     tmp_set = set()
#     print(f'i는 {i}')
#     for j in range(6):
#         tmp = ''
#         for k in range(4):
#             # print(f'k는 {bin(1 << k)}')
#             ## i = 1001 이다 하면 relation[j]의 원소 0번째랑 네번째를 더해야 하잖아. 
#             ## 그래서 k 를 range(4로 돌면서) 비트연산으로 했을 때 둘이 겹치는 부분이 있는가 
#             # i = 1001 이면 k 비트연산 했을 때 k=0이면 1이니까 이 원소 포함해야 되서 더해야 하잖아.
#             # 그리고 k=1 이면 10이니까 해당 수 더하기 
#             # 그러니까 k의 역할을 i의 각자리수를 확인하면서 거기가 1인 친구를 relation 요소의 인덱스를 tmp에 더하는 역할 
#             ## 1 << k = 0001, 0010, 0100, 1000
#             if i & (1 << k):
#                 print("==맞대==")
#                 print(bin(i), bin(1<<k), str(relation[j][k]))
#                 tmp += str(relation[j][k])
         
#         # print(tmp)
#         tmp_set.add(tmp)
#         # print(tmp_set)
#     # print(tmp_set)

def solution2(relation):
    answer_list = list()
    for i in range(1, 1 << len(relation[0])):
        tmp_set = set()
        for j in range(len(relation)):
            tmp = ''
            for k in range(len(relation[0])):
                if i & (1 << k):
                    tmp += str(relation[j][k])
            tmp_set.add(tmp)

        if len(tmp_set) == len(relation):
            not_duplicate = True
            for num in answer_list:
                if (num & i) == num:
                    print(bin(num))
                    print(bin(i))
                    print(bin(num & i))
                    not_duplicate = False
                    break
            if not_duplicate:
                answer_list.append(i)
    return len(answer_list)



# print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
print(solution2([['a', 'aa'], ['aa', 'a'], ['a', 'a']])) ## 0, 이거 근데 왜 통과? 
print(solution([['a', 'aa'], ['aa', 'a'], ['a', 'a']])) ## 1 

