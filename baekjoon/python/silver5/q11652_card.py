import sys
input = sys.stdin.readline

n = int(input())
numbers = {}
for _ in range(n):
    num = int(input())
    if num in numbers:
        numbers[num] = (num, numbers[num][1] + 1)
    else:
        numbers[num] = (num, 1)


numbers = list(numbers.values())
numbers.sort(key=lambda x : (-x[1], x[0]))
print(numbers[0][0])

