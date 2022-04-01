for _ in range(int(input())):
    data = list(map(int, input().split()))
    stu_cnt = data[0]
    data = data[1:]
    average = sum(data) / stu_cnt
    cnt_over_average = 0
    for d in data:
        if d > average :
            cnt_over_average += 1
    # print(format(round((cnt_over_average / stu_cnt) * 100, 3), '.3f'), "%") 
    value = round((cnt_over_average / stu_cnt) * 100, 3)
    print(f"{value:.3f}%")

