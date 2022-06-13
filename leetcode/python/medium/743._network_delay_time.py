## 512 ms, 	16.6 MB
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for i in range(n+1)]
        for s, d, t in times:
            graph[s].append((t, d))
        
        INF = int(1e9)
        q = []
        dis = [INF] * (n+1)
        
        dis[k] = 0 
        heapq.heappush(q, (0, k))
        
        while q :
            t, start = heapq.heappop(q)
            if dis[start] < t:
                continue
            for c, d in graph[start]:
                cost = t + c
                if cost < dis[d]:
                    dis[d] = cost
                    heapq.heappush(q, (cost, d))
        
        if INF in dis[1:]:
            return -1
        
        ans = -1
        for i in range(1, n+1):
            if i == k:
                continue
            if ans < dis[i]:
                ans = dis[i]
        
        if ans == INF:
            return -1
        return ans
        