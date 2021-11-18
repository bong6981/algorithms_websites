def solution(a, b):
    days = b
    d = { 0:'FRI', 1:'SAT', 2:'SUN', 3:'MON', 4:'TUE', 5:'WED', 6:'THU'}

    if a != 1:
        for i in range(1, a):
            if i == 2 :
                days += 29 
            elif i in [4, 6,9,11] :
                days += 30 
            else :
                days += 31
    
    return d[( days - 1 ) % 7]

#실제 2016년 1월 1일이 금요일이라 진짜 주어진 날짜를 구하는 방법 
import datetime
def solution2(a, b):
    week = 'MON,TUE,WED,THU,FRI,SAT,SUN'.split(',')
    return week[datetime.datetime(2016,a,b).weekday()]

print(solution2(5,24))
