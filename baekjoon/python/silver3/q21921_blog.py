# https://www.acmicpc.net/problem/21921
def solution():
    n, x = map(int, input().split())
    visitors = list(map(int, input().split()))
    start = 0
    end = start + x - 1
    prev = 0
    for i in range(x):
        prev += visitors[i]

    record = [prev]
    start += 1
    end += 1
    while end < n :
        prev = prev - visitors[start-1] + visitors[end]
        record.append(prev)
        start += 1
        end += 1
    
    record.sort(reverse=True)
    if record[0] == 0 :
        print("SAD")
        return
    print(record[0])
    print(record.count(record[0]))

solution()
