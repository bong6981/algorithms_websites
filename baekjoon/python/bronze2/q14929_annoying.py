def solution():
    n = int(input())
    array = list(map(int, input().split()))
    array.reverse()
    sum = 0
    number = array[0]
    for a in array[1:]:
        sum += (number) * a
        number += a
    return sum

print(solution())
