def solution(n, info):
    global ans_score, ans
    ans = [0] * (11)
    ans_score = 0
    
    def shoot(i, left, score, ret, appeach):
        global ans_score, ans

        if i == 11:
            ret[10] = left

            if score - appeach > ans_score:
                ans_score = score - appeach
                ans = ret
            elif ans_score == score - appeach:
                for i in range(10, -1, -1):
                    if ret[i] == ans[i]:
                        continue
                    if ret[i] > ans[i]:
                        ans = ret
                    break
            return
        
        #이기기
        if info[i] < left:
            shoot(i+1, left - (info[i] + 1), score + 10 - i, ret + [info[i] + 1], appeach)
        
        #지기 
        if info[i] == 0 :
            shoot(i+1, left, score, ret+[0], appeach)
        else:
            shoot(i+1, left, score, ret+[0], appeach + 10 - i)
        
    shoot(0, n, 0, [], 0)
    if ans_score == 0 or ans == [0] * 11:
        return [-1]
    return ans

# print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
