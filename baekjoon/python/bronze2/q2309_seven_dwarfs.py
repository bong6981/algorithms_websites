dwarfs_height = [int(input()) for _ in range(9)]
dwarfs_height.sort()

ans = []
def acc(picked_dwarfs, acc_total, start_idx):
    global ans
    if 7 - len(picked_dwarfs) > 9 - start_idx : 
        return 0
    if len(picked_dwarfs) == 7 and acc_total == 100:
        ans = picked_dwarfs
        return 1

    for i in range(start_idx, 9):
        picked_dwarfs.append(dwarfs_height[i])
        if acc(picked_dwarfs, acc_total + dwarfs_height[i], i+1):
            return True
        picked_dwarfs.pop()
    
    return 0

acc([], 0, 0)
for d in ans:
    print(d)

