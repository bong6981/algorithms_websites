def solution(phone_number):
    return '*' * (len(phone_number) - 4) + phone_number[-4:]

print('*' * (len('hell') -4))

def solution_old(phone_number):
    phone_list = list(phone_number)
    n = len(phone_list)
    for i in range(n-4):
        phone_list[i] = '*'
    str_phone_list = ''.join(phone_list)
    answer = str_phone_list
    return answer
