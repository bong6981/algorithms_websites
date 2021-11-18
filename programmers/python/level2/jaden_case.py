def solution(s):
    a = s.lower().split(" ")
    for i in range(len(a)) :
        if a[i] == '' :
           continue
        c = list(a[i])
        c[0] = c[0].upper()
        a[i] = "".join(c)
    return " ".join(a)

def solution2(s):
    a = s.split(" ")
    for i, s in enumerate(a) :
        a[i] = s.capitalize()
    return " ".join(a) 

def solution3(s):
    print(list(s.split(" ")))
    return " ".join( word.capitalize() for word in s.split(" ")) 

print(solution3("3people      unFollowed me"))
print(list(solution3("   ")))


# print("hello world 3world".capitalize())
# print("hello world 3world".title())
# print("3world".title())
# print("3world".capitalize())
# print(" ".capitalize())
# print("heLlo".capitalize())
# print("heLlo".title())




