## https://programmers.co.kr/learn/courses/30/lessons/42895
def solution(N, number):
    if N == number:
        return 1

    dp = []
    dp.append(set())
    for i in range(1, 9):
        s = set()
        s.add(int(str(N)*i))
        if int(str(N) * i) == number :
            return i
        for j in range(1, i):
            s1 = dp[j]
            s2 = dp[i-j]
            for x in s1:
                for y in s2:
                    s.add(x+y)
                    s.add(x-y)
                    s.add(x*y)
                    if y != 0:
                        s.add(x//y)
                    if number in s:
                        return i
        dp.append(s)
    return -1    


print(solution(5, 12))
print(solution(2, 11))
