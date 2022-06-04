# https://leetcode.com/problems/range-sum-query-2d-immutable/
# 304. Range Sum Query 2D - Immutable

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.m = matrix
        self.R, self.C = len(matrix), len(matrix[0])
        self.ps = [[0 for j in range(self.C)] for i in range(self.R)]
        for i in range(self.R):
            for j in range(self.C):
                if i == 0:
                    self.ps[i][j] = self.m[i][j] + self.ps[i][j-1]
                elif j == 0:
                    self.ps[i][j] = self.m[i][j] + self.ps[i-1][j]
                else:
                    self.ps[i][j] = self.m[i][j] + self.ps[i][j-1] + self.ps[i-1][j] - self.ps[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.ps[-1][-1]
        aboveRows = 0 if row1 == 0 else self.ps[row1-1][-1]
        belowRows = 0 if row2 == self.R-1 else self.ps[-1][-1] - self.ps[row2][-1]
        beforeCols = 0 if col1 == 0 else self.ps[row2][col1-1] - (0 if row1 == 0 else self.ps[row1-1][col1-1])
        afterCols = 0 if col2 == self.C-1 else (self.ps[row2][-1] - self.ps[row2][col2]) - (0 if row1 == 0 else self.ps[row1-1][-1] - self.ps[row1-1][col2])
        
        #print(total, aboveRows, belowRows, beforeCols, afterCols)
        return total - aboveRows - belowRows - beforeCols - afterCols
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)