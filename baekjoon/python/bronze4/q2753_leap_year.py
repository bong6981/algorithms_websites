year = int(input())

printed = False
if not year % 4 :
    if (year % 100) or not (year % 400):
        print("1")
        printed = True
        
if not printed :
    print("0")


