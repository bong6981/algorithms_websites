max_value = 0
max_idx = 0 
for i in range(1, 10):
    num = int(input())
    if num > max_value:
        max_value = num
        max_idx = i
print(max_value)
print(max_idx)
