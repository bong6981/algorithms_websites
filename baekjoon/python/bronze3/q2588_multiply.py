# first_input = int(input())
# second_input = input()

# ans_third = first_input * int(second_input[2])
# ans_fourth = first_input * int(second_input[1])
# ans_fifth = first_input * int(second_input[0])
# ans_sixth = ans_third + ans_fourth * 10 + ans_fifth * 100

# print(ans_third)
# print(ans_fourth)
# print(ans_fifth)
# print(ans_sixth)

## 이전에 푼 코드가 낫다 
input1 =int(input())
input2 = list(map(int, list(input())))

ans = 0
for i, num in enumerate(reversed(input2)):
    num *= input1
    print(num)
    ans += num * (10 ** i)

print(ans)

## 똑똑이 수학적으로 풀었네 
# A = int(input())
# B = int(input())

# print(A * (B % 10))
# print(A * ((B % 100) // 10))
# print(A * (B // 100))
# print(A * B)

print(4/2)