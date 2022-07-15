from collections import deque
import heapq
def solution(nodeinfo):

    info = []
    sorted_nodeinfo = []
    for i in range(len(nodeinfo)):
        now = nodeinfo[i]
        print(now, (now[1], i))
        sorted_nodeinfo.append((now[1], i+1))

    sorted_nodeinfo.sort(reverse = True)
    print(sorted_nodeinfo)
    child_info = [[-1, -1] for _ in range(len(nodeinfo)+1)]


    for i in range(1, len(sorted_nodeinfo)+1):
        now = sorted_nodeinfo[i]
        print("----")
        print(now)
        # find _ p
        for j in range(i-1, -1, -1):
            p = sorted_nodeinfo[j][1]
            print(sorted_nodeinfo[j], child_info[p])
            if child_info[p][0] == -1:
                print("left")
                now_x = nodeinfo[p][0]
                if nodeinfo[p][0] > now_x:
                    child_info[p][0] = now[1]
                    continue
            if child_info[p][1] == -1:
                print("right")
                if nodeinfo[p][1] < now_x:
                    child_info[p][1] = now[1]
    
    print(child_info)

    answer = [[]]
    return answer

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))
