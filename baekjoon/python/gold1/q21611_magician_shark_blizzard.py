# https://www.acmicpc.net/problem/21611
import sys
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    
    #상어위치
    sharks = ((n-1) // 2, (n-1) // 2)

    #순서 그래프 채우기 
    order_board = [[0] * n for _ in range(n)]
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x = 0
    y = 0
    num = n * n - 1
    d = 0
    while True:
        order_board[x][y] = num
        num -= 1
        if num == 0 :
            break
        nextx = x + moves[d][0]
        nexty = y + moves[d][1]
        if not (0 <= nextx < n and 0 <= nexty < n and order_board[nextx][nexty] == 0) :
            d = change_dir(moves, d)
            nextx = x + moves[d][0]
            nexty = y + moves[d][1]
        x = nextx
        y = nexty
    order_list = [() for _ in range(n**2)]
    for i in range(n):
        for j in range(n):
            order_list[order_board[i][j]] = (i, j)
    

    # 그래프 채우기 
    board = []
    for _ in range(n):
        r = list(map(int, input().split()))
        board.append(r)

    beads_in_order = [0]
    for i, o in enumerate(order_list[1:], 1):
        if board[o[0]][o[1]] == 0 and (o[0], o[1]) != sharks:
            break
        beads_in_order.append(board[o[0]][o[1]])
    


    boom_count = [0 for _ in range(4)]
    for _ in range(m):
        d, s = map(int, input().split())

        magic_ds = [(), (-1, 0), (1, 0), (0, -1), (0, 1)]
        magic_d = magic_ds[d]
        nx = sharks[0]
        ny = sharks[1]

        # 구슬 파괴
        for _ in range(s):
            nx += magic_d[0]
            ny += magic_d[1]
            num = order_board[nx][ny]
            if len(beads_in_order) - 1 >= num :
                beads_in_order[num] = -1
        beads_in_order = list(filter(lambda x : x != -1, beads_in_order))


        if len(beads_in_order) <= 1 :
            continue
        
        # 구슬 폭발 
        while True:
            ## 주의 
            if len(beads_in_order) <= 1 :
                break
            i = 2
            to_boom_list = []
            now = beads_in_order[1]  
            to_boom = [1]
            while True:
                if i >= len(beads_in_order) :
                    break
                if beads_in_order[i] == now:
                    to_boom.append(i)
                else:
                    if len(to_boom) >= 4 :
                        to_boom_list.extend(to_boom)
                        boom_count[now] += len(to_boom)
                    now = beads_in_order[i]
                    to_boom = [i]
                i += 1
            
            if len(to_boom) >= 4 :
                to_boom_list.extend(to_boom)
                boom_count[now] += len(to_boom)
        
            if len(to_boom_list) == 0 :
                break
            to_boom_set = set(to_boom_list)
            beads_in_order =  [ beads_in_order[i] for i in range(0, len(beads_in_order)) if i not in to_boom_set] 
            
        # 구슬 변화 
        new_beads_in_order = [beads_in_order[0]]
        now = []

        if len(beads_in_order) > 1:
            for i, bead in enumerate(beads_in_order[1:], 1):
                if len(now) == 0 or bead == now[0]: 
                    now.append(bead)
                    continue
                new_beads_in_order.append(len(now))
                new_beads_in_order.append(now[0])
                now = [bead]
                        
            new_beads_in_order.append(len(now))
            new_beads_in_order.append(now[0])             
            
        if len(new_beads_in_order) > n**2 :
            new_beads_in_order = new_beads_in_order[:n**2]
        
        beads_in_order = new_beads_in_order
    return sum(i * v for i, v in enumerate(boom_count[1:], 1))

def change_dir(moves, d):
    d += 1
    if d >= len(moves) :
        return 0
    return d

print(solution())

'''
예외 케이스 
3 1
1 1 1
1 0 1
1 1 1
3 1
'''
