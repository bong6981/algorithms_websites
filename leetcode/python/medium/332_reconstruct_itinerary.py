#112 ms,15.1 MB
# https://leetcode.com/problems/reconstruct-itinerary/
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        info = defaultdict(list)
    
        tickets.sort()
        for i, t in enumerate(tickets):
            info[t[0]].append(i) 

        used = [0] * (len(tickets))

        def reconstruct(start, arr):
            if 0 not in used:
                return arr[:]

            for t_idx in info[start]:
                if not used[t_idx]:
                    used[t_idx] = 1
                    ret = reconstruct(tickets[t_idx][1], arr+[t_idx])
                    if ret != []:
                        return ret
                    used[t_idx] = 0

            return []

        order = reconstruct("JFK", [])
        ans = []
        for t in order:
            ans.append(tickets[t][0])
        ans.append(tickets[order[-1]][1])
        return ans 


## 책 풀이 
def sol(tickets):
    graph = defaultdict(list)
    for a, b in sorted(tickets):
        graph[a].append(b)
    
    route = []
    def dfs(s):
        while graph[s]:
            dfs(graph[a].pop(0))
        route.append(a)

    dfs("JFK")
    return route[::-1]


