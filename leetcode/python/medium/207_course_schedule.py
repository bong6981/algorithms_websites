# 112 ms, 15.3 MB
# https://leetcode.com/problems/course-schedule/
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        parent = []
        for i in range(numCourses):
            parent.append(i)
        
        def find_p(x):
            if x != parent[x]:
                parent[x] = find_p(parent[x])
            return parent[x]
        
        def union(x, y):
            x = find_p(x)
            y = find_p(y)
            if x < y :
                parent[y] = x
            else:
                parent[x] = y
        
        indegree = [0] * (numCourses)
        graph = [[] for _ in range(numCourses)]
        
        for x, y in prerequisites:
            graph[x].append(y)
            indegree[y] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        for i in range(numCourses):
            if not q :
                return False
            now = q.popleft()
            for des in graph[now]:
                indegree[des] -= 1
                if indegree[des] == 0:
                    q.append(des)
        return True        
            
            
            
        