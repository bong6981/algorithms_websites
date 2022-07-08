
def hex_to_dec(h):
    info = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    ret = 0
    for i in range(len(h)):
        x = info.index(h[i])
        x *= 16 ** (len(h) - 1 - i)
        ret += x
    return ret

def oct_to_dec(o):
    ret = 0
    for i in range(len(o)):
        x = int(o[i])
        x *= 8 ** (len(o)-1-i)
        ret += x
    return ret

# X = input()
# if X[0] == '0':
#     if X[1] == 'x':
#         print(hex_to_dec(X[2:]))
#     else:
#         print(oct_to_dec(X[1:]))
# else:
#     print(X)

X = input()
if X[0] == '0':
    if X[1] == 'x':
        print(int(X, 16))
    else:
        print(int(X, 8))
else:
    print(X)
