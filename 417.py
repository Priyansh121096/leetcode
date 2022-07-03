# https://leetcode.com/problems/pacific-atlantic-water-flow/
# 417. Pacific Atlantic Water Flow

from collections import deque

class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        M, N = len(grid), len(grid[0])
        
        def bfs(queue):
            visited = [[False for _ in range(N)] for __ in range(M)]
            
            while queue:
                i, j = queue.popleft()
                visited[i][j] = True
                
                if (0 <= i-1 < M and 0 <= j < N) and not visited[i-1][j] and grid[i-1][j] >= grid[i][j]:
                    queue.append((i-1, j))
                if (0 <= i+1 < M and 0 <= j < N) and not visited[i+1][j] and grid[i+1][j] >= grid[i][j]:
                    queue.append((i+1, j))
                if (0 <= i < M and 0 <= j-1 < N) and not visited[i][j-1] and grid[i][j-1] >= grid[i][j]:
                    queue.append((i, j-1))
                if (0 <= i < M and 0 <= j+1 < N) and not visited[i][j+1] and grid[i][j+1] >= grid[i][j]:
                    queue.append((i, j+1))
                    
            return visited
        
        pacific = [(0, j) for j in range(N)]
        pacific.extend([(i, 0) for i in range(M)])
        pacific = bfs(deque(pacific))
        
        atlantic = [(M-1, j) for j in range(N)]
        atlantic.extend([(i, N-1) for i in range(M)])
        atlantic = bfs(deque(atlantic))
        
        out = []
        for i in range(M):
            for j in range(N):
                if pacific[i][j] and atlantic[i][j]:
                    out.append([i, j])
                    
        return out
    
# DFS
class Solution:
    def dfs(self, grid, i, j, reachable):
        M, N = len(grid), len(grid[0])
        
        if not (0 <= i < M and 0 <= j < N):
            return reachable
        
        reachable.add((i, j))
        
        dirs = [
            (-1, 0),  # North
            (1, 0),   # South
            (0, -1),  # East
            (0, 1),   # West
        ]
        for x, y in dirs:
            ni, nj = i+x, j+y
            if (0 <= ni < M and 0 <= nj < N) and (ni, nj) not in reachable and (grid[ni][nj] >= grid[i][j]):
                reachable = self.dfs(grid, ni, nj, reachable)
                
        return reachable
        
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        M, N = len(grid), len(grid[0])
        
        pacific = set()
        for j in range(N):
            pacific.add((0, j))
            
        for i in range(M):
            pacific.add((i, 0))
            
        all_pacific = set()
        for i, j in pacific:
            all_pacific = self.dfs(grid, i, j, all_pacific)
            
        atlantic = set()
        for j in range(N):
            atlantic.add((M-1, j))
            
        for i in range(M):
            atlantic.add((i, N-1))
            
        all_atlantic = set()
        for i, j in atlantic:
            all_atlantic = self.dfs(grid, i, j, all_atlantic)
            
        return all_pacific.intersection(all_atlantic)