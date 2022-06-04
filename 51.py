# https://leetcode.com/problems/n-queens/
# 51. N-Queens

# Solution 1 (AC)
class Solution:
    @staticmethod
    def ansString(grid):
        s, b = [], []
        for i in range(len(grid)):
            srow, brow = [], []
            for j in range(len(grid[0])):
                srow.append("." if grid[i][j] is False else "Q")
                brow.append("0" if grid[i][j] is False else "1")
            s.append("".join(srow))
            b.append("".join(brow))
            
        b = int("".join(b), 2)
        return s, b
                
    
    def helper(self, grid, row, cols, prevCols, n):        
        if row == n:
            s, b = self.ansString(grid)
            
            if b not in self.mem:
                self.mem.add(b)
                self.out.append(s)
            
            return
            
		# Since we mutate the cols set inside the loop, the order can change and can
		# lead to repetitions of some elements at the cost of missed iterations of others.
		# (This cost me a lot of time)
        for col in cols.copy():
            def isValid(col, prevCols):
                N = len(prevCols)
                for i, pc in enumerate(prevCols):
                    if col in (pc, pc - (N-i), pc + (N-i)):
                        return False
                    
                return True
                    
            if isValid(col, prevCols):
                grid[row][col] = True
                cols.remove(col)
                prevCols.append(col)
                self.helper(grid, row+1, cols, prevCols, n)
                prevCols.pop()
                cols.add(col)
                grid[row][col] = False
            
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.out, self.mem = [], set()
        g = [[False for j in range(n)] for i in range(n)]
        cols = set(range(n))
        self.helper(g, 0, cols, [], n)
        return self.out