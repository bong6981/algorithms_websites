input1 =int(input())
input2 = list(map(int, list(input())))

ans = 0
for i, num in enumerate(reversed(input2)):
    num *= input1
    print(num)
    ans += num * (10 ** i)

print(ans)

