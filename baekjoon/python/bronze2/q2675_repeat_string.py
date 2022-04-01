for _ in range(int(input())):
    num, string = input().split()
    num = int(num)
    for c in string:
        print(c*num, end="")
    print()
