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
        