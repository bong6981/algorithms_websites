n, x = map(int, input().split())
for num in list(map(int, input().split(" "))):
    if num < x :
        print(num, end=" ")
