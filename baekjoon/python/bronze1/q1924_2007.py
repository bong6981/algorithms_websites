import sys
input = sys.stdin.readline

month, day = map(int, input().split())

days = day
days_per_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(1, month):
    days += days_per_month[i]

days_of_week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
print(days_of_week[days % 7])
