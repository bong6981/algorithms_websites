## https://school.programmers.co.kr/learn/courses/30/lessons/49994

def went_add(went, p1, p2):
    if (p1[0], p1[1], p2[0], p2[1]) in went:
        return
    if (p2[0], p2[1], p1[0], p1[1]) in went:
        return 
    went.add((p1[0], p1[1], p2[0], p2[1]))
    return 

def solution(dirs):
    moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    
    r, c = 0, 0 
    went = set()
    for dir in dirs:
        if(dir == "U"):
            if r + 1 <= 5:
                went_add(went, (r, c), (r+1, c))
                r += 1
        elif(dir == "D"):
            if r - 1 >= -5:
                went_add(went, (r, c), (r-1, c))
                r -= 1
        elif(dir == "R"):
            if c + 1 <= 5:
                went_add(went, (r, c), (r, c+1))
                c += 1
        elif(dir == "L"):
            if c - 1 >= -5:
                went_add(went, (r, c), (r, c-1))
                c -= 1
    return len(went)


## 양방향 다 더하는 풀이 
def solution(dirs):
    s = set()
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x, y = nx, ny
    return len(s)//2
