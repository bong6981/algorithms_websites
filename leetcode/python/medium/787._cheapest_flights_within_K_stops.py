## 161 ms, ## 15.4 MB
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
            
            board = [[] for _ in range(n)]
            for s, des, price in flights:
                board[s].append((des, price))
            
            q = [(0, src, 0)]
            visited = [0] * n
            
            while q:
                p, s, cnt = heapq.heappop(q)
                if s == dst:
                    return p
                if cnt > k:
                    continue
                
                if visited[s] <= cnt:
                    continue

                for des, price in board[s]:
                    heapq.heappush(q, (p + price, des, cnt+1))
            return -1
            
           
                