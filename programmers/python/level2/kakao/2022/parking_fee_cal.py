# https://programmers.co.kr/learn/courses/30/lessons/92341?language=python3
import math

def solution(fees, records):
    min_time, min_fee, unit_time, unit_fee = fees
    info = {}
    answer = {}
    for record in records:
        print(record)
        time, num, status = record.split(" ")
        num = int(num)
        if status == "IN" :
            info[num] = time
        else:
            in_h, in_m = map(int, info[num].split(":"))
            out_h, out_m = map(int, time.split(":"))
            time = (out_h * 60 + out_m) - (in_h * 60 + in_m)
            if num in answer:
                answer[num] += time
            else:
                answer[num] = time
            del(info[num])
        print(answer)

    if len(info) > 0 :
        for i in info.keys():
            print(i, info[i])
            in_h, in_m = map(int, info[i].split(":"))
            time = (23 * 60 + 59) - (in_h * 60 + in_m)
            if i in answer:
                answer[i] += time
            else:
                answer[i] = time
            print(answer)


    total = []
    for ans in answer.keys():
        print(ans, answer[ans])
        time = answer[ans]
        if time <= min_time :
            total.append((ans, min_fee))
        else:
            total.append((ans, min_fee + math.ceil((time - min_time) / unit_time) * unit_fee))

    total.sort()
    answer = []
    for t in total:
        num, fee = t
        answer.append(fee)
    return answer

# print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
# print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
