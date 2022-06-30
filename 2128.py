# https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/
# 2128. Remove All Ones With Row and Column Flips

class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        M, N = len(grid), len(grid[0])
        
        for r in range(1, M):
            if not (grid[r] == grid[0] or grid[r] == [1 - x for x in grid[0]]):
                return False
            
        return True