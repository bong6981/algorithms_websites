from itertools import combinations
import sys
input = sys.stdin.readline

while True:
    numbers = list(map(int, input().split()))
    if numbers[0] == 0:
        break

    k = numbers[0]
    numbers = numbers[1:]
    for cb in combinations(numbers, 6):
        picked_numbers = sorted(list(cb))
        print(*picked_numbers)
    print()
