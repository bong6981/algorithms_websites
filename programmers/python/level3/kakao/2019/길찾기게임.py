def find_max_y(nodes, start, end):
    max_v = -1
    ret = -1
    for i in range(start, end+1):
        if nodes[i][1] > max_v:
            max_v = nodes[i][1]
            ret = i 
    return ret 

def solution(nodeinfo):
    nodes = []
    for i, info in enumerate(nodeinfo):
        nodes.append((info[0], info[1], i))

    
    nodes.sort(key=lambda x: x[0])
    print(nodes)
    
    def seperate(nodes, start, end, prev_arr, post_arr):
        if start < 0 or start > end or end >= len(nodes):
            return
        root = find_max_y(nodes, start, end)
        prev_arr.append(nodes[root][2]+1)
        seperate(nodes, start, root-1, prev_arr, post_arr)
        seperate(nodes, root+1, end, prev_arr, post_arr)
        post_arr.append(nodes[root][2]+1)
    
    prev_arr = []
    post_arr = []
    seperate(nodes, 0, len(nodes)-1, prev_arr, post_arr)
    return [prev_arr, post_arr]

# print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))
print(solution([[5,3]]))
