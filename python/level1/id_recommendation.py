
def solution(new_id):
    new_id = new_id.lower()
    exclude = "~!@#$%^&*()=+[{]}:?,<>/"
    new_id = ''.join(x for x in new_id if x not in exclude)
    while '..' in new_id :
        new_id = new_id.replace('..', '.')
    if  len(new_id) >= 1 and new_id[0] == '.' :
        new_id = new_id.lstrip('.')    
    if len(new_id) >= 1 and new_id[-1] == '.' : 
        new_id = new_id.rstrip('.')
    if len(new_id) == 0 :
        new_id = 'a'
    if len(new_id) >= 16 :
        new_id = new_id[:15]
        if new_id[-1] == '.' : 
            new_id = new_id.rstrip('.')
    while len(new_id) <= 2 :
        new_id += new_id[-1]
    return new_id



print(solution("abcdefghijklmn.p"))