def solution():
    n, k = map(int, input().split(" "))
    numbers = []
    ## 다른 이 풀이에서 numbers = list(range(1, n+1))로 간단하게 만들 수 있다.
    for i in range(1, n+1):
        numbers.append(i)
    
    idx = 0
    answer = []
    while numbers != []:
        cnt = 1
        while True:
            if idx==len(numbers) :
                idx = 0
            if cnt == k:
                answer.append(numbers[idx])
                numbers = numbers[:idx] + numbers[idx+1:]
                break
            cnt += 1
            idx += 1
    
    print("<", end = "")
    for i, a in enumerate(answer) :
        if i == len(answer)-1 :
            print(a, end=">")
        else:
            print(a, end=", ")

# solution()

def other():
    n, k = map(int, input().split())
    answer = []
    numbers = list(range(1, n+1))
    ## 어차피 n번 빼니까 
    for i in range(n):
        to_delete = (k-1) % len(numbers)
        answer.append(numbers[to_delete])
        # 어차피 그 다음 친구부터 세니까 그 친구를 맨 앞으로
        numbers = numbers[to_delete+1:] + numbers[:to_delete]
    # print(str(answer)) ## [3, 6, 2, 7, 5, 1, 4]
    print("<"+str(answer)[1:-1]+">")

other()
