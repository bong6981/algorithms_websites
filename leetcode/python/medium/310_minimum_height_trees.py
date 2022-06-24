#556 ms, 	24.1 MB
# https://leetcode.com/problems/minimum-height-trees/
from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if edges == []:
            return [0]
        
        if len(edges) == 1:
            return edges[0]
        
        INF = 1e9
        graph = [[] * (n) for _ in range(n)]
        
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        cnt = 0
        q = deque([])
        for i in range(n):
            if len(graph[i]) == 1:
                q.append(i)
        while True:
            new_q = deque()
            while q:
                x = q.popleft()
                cnt += 1
                des = graph[x][0]
                graph[des].remove(x)
                if len(graph[des]) == 1:
                    new_q.append(des)
                
            q = new_q
            if cnt + len(new_q) == n:
                break

        return list(q)
            
        