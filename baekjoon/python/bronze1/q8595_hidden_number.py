n = int(input())
word = input().rstrip()
ret = 0

num_str = ''
for c in word:
    if c.isdigit():
        num_str += c
    elif num_str != '':
        ret += int(num_str)
        num_str = ''

if num_str != '':
    ret += int(num_str)
            
print(ret)
