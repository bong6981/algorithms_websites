def solution(lottos, win_nums):
    lottos.sort(reverse = True)
    win_nums.sort(reverse = True)
    i = 0
    z = 0
    ranking = { 6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    for lotto in lottos :
        if lotto == 0 :
            z = len(lottos) -  lottos.index(lotto)
            break
        for win_num in win_nums :
            if lotto == win_num :
                i += 1
            elif lotto > win_num :
                break        
    answer = []
    max = i + z
    min = i 
    answer.append(ranking[max])
    answer.append(ranking[min])
    return answer

def solution_2(lottos, win_numbs) :
    rank = [ 6, 6, 5, 4, 3, 2, 1]
    cnt_0 = lottos.count(0)
    ans = len([x for x in lottos if x in win_numbs])
    return [rank[ans + cnt_0], rank[ans]]

def solution_3(lottos, win_numbs) :
    rank = [ 6, 6, 5, 4, 3, 2, 1]
    min = len(set(lottos) & set(win_numbs))
    return [ rank[min + lottos.count(0)], rank[min]]
lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]
print(solution_2(lottos, win_nums))