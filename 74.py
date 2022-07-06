# https://leetcode.com/problems/search-a-2d-matrix/
# 74. Search a 2D Matrix

from bisect import bisect_left

class Solution:
    def searchMatrix(self, m: List[List[int]], t: int) -> bool:
        firstCol = [row[0] for row in m]
        rowIdx = bisect_left(firstCol, t)
        if rowIdx < len(m) and m[rowIdx][0] == t:
            return True
        rowIdx -= 1
        
        colIdx = bisect_left(m[rowIdx], t)
        return colIdx < len(m[0]) and m[rowIdx][colIdx] == t