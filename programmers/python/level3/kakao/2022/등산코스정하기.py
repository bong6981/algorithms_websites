import heapq

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n+1)]
    for p1, p2, cost in paths:
        graph[p1].append([p2, cost])
        graph[p2].append([p1, cost])
        # if p2 in gates:
        #     graph[p1].append([p2, cost, True, False])
        # elif p2 in summits:
        #     graph[p1].append([p2, cost, False, True])
        # else:
        #     graph[p1].append([p2, cost, False, False])

        # if p1 in gates:
        #     graph[p2].append([p1, cost, True, False])
        # elif p1 in summits:
        #     graph[p2].append([p1, cost, False, True])
        # else:
        #     graph[p2].append([p1, cost, False, False])


    INF = 10000000 + 1
    ans = [-1, INF]
    costs = [INF] * (n+1)

    gates = set(gates)
    summits = set(summits)

    for start in gates:
        q = []
        heapq.heappush(q, (0,start))
        costs[start] = 0
        
        while q:
            val, pos = heapq.heappop(q)
          
            if costs[pos] < val:
                continue
            
            for des in graph[pos]:
                ## gate 인 경우 
                if des[0] in gates:
                    continue
                cost = max(des[1], val)
                ## path인경우 
                if cost < costs[des[0]]:
                    costs[des[0]] = cost
                    if not des[0] in summits:
                        heapq.heappush(q, (cost, des[0]))
        
    for summit in summits:
        if costs[summit] < ans[1]:
            ans = [summit, costs[summit]]
        elif costs[summit] == ans[1]:
            ans[0] = min(ans[0], summit)
        
    return ans
