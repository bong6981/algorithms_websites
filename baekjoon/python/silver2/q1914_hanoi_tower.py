def hanoi(n, origin, des, stop):
    global log, to_print
    if n == 1:
        print(origin, des)
        return 
    
    hanoi(n-1, origin, stop, des)
    print(origin, des)
    hanoi(n-1, stop, des, origin)

n = int(input())
cnt = (2**n)-1
print(cnt)
if n <= 20 :
    hanoi(n, 1, 3, 2)
