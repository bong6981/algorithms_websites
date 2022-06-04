## 367ms, 16.4MB
# https://leetcode.com/problems/number-of-islands/submissions/
class Solution:
    def search(self, r, c, visited, graph):
        visited[r][c] = 1
        moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for move in moves:
            nr = r + move[0]
            nc = c + move[1]
            if 0 <= nr < len(graph) and 0 <= nc < (len(graph[0])):
                if not visited[nr][nc] and graph[nr][nc] == "1":
                    self.search(nr, nc, visited, graph)
        
    
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not visited[i][j] :
                    ans += 1;
                    self.search(i, j, visited, grid)
        return ans
        