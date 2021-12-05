from collections import deque
def solution() :
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    
    arrs = deque([arr])
    white = 0
    blue = 0
    while arrs:
        arr = arrs.popleft()
        n = len(arr)
        print(arr)
        blue_is = False
        white_is = False
        for i in range(len(arr)):
            if 0 in arr[i] :
                white_is = True
            if 1 in arr[i] :
                blue_is = True
            if blue_is and white_is:
                break

        if blue_is and white_is:
            arrs.extend(divde(arr, n)) 
            continue
        if white_is :
            white += 1
        else:
            blue += 1
    
    print(white)
    print(blue)


def divde(arr, n):
    answer = []
    c = n // 2

    row = []
    row2 = []
    row3 = []
    row4 = []
    for i in range(c):
        col = []
        col2 = []
        for j in range(c):
            col.append(arr[i][j])
        for j in range(c, n):
            col2.append(arr[i][j])
        row.append(col)
        row2.append(col2)
    answer.append(row)
    answer.append(row2)

    for i in range(c, n):
        col3 = []
        col4 = []
        for j in range(c):
            col3.append(arr[i][j])
        for j in range(c, n):
            col4.append(arr[i][j])
        row3.append(col3)
        row4.append(col4)
    answer.append(row3)
    answer.append(row4)

    return answer


solution()
