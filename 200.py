# https://leetcode.com/problems/number-of-islands/
# 200. Number of Islands

# DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])
        
        def dfs(i, j):
            if not (0 <= i < M and 0 <= j < N):
                return
            
            grid[i][j] = '#'
            if (0 <= i-1 < M and 0 <= j < N) and grid[i-1][j] == '1':
                dfs(i-1, j)
            if (0 <= i+1 < M and 0 <= j < N) and grid[i+1][j] == '1':
                dfs(i+1, j)
            if (0 <= i < M and 0 <= j-1 < N) and grid[i][j-1] == '1':
                dfs(i, j-1)
            if (0 <= i < M and 0 <= j+1 < N) and grid[i][j+1] == '1':
                dfs(i, j+1)
            
        count = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
                    
        return count


# BFS
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])
        
        def bfs(i, j):
            queue = deque([(m, n)])
            while queue:
                i, j = queue.popleft()

                if grid[i][j] != '1':
                    continue
                grid[i][j] = '2'

                dirs = [
                    (-1, 0),
                    (1, 0),
                    (0, -1),
                    (0, 1),
                ]
                for x, y in dirs:
                    ni, nj = i+x, j+y
                    if 0 <= ni < M and 0 <= nj < N and grid[ni][nj] == '1':
                        queue.append((ni, nj))
            
        count = 0
        for m in range(M):
            for n in range(N):
                if grid[m][n] == '1':
                    bfs(m, n)    
                    count += 1
                    
        return count