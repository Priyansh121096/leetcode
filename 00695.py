# https://leetcode.com/problems/max-area-of-island/
# 695. Max Area of Island

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        
        def dfs(i, j, count):
            if not (0 <= i < M and 0 <= j < N):
                return count
            
            if grid[i][j] != 1:
                return count
            
            count += 1
            grid[i][j] = 2
            
            for x, y in ((0, -1), (-1, 0), (1, 0), (0, 1)):
                ni, nj = i+x, j+y
                if 0 <= ni < M and 0 <= nj < N and grid[ni][nj] == 1:
                    count = dfs(ni, nj, count)
                    
            return count
        
        maxCount = -inf
        for i in range(M):
            for j in range(N):
                maxCount = max(maxCount, dfs(i, j, 0))
                
        return maxCount