# https://leetcode.com/problems/convert-1d-array-into-2d-array/
# 2022. Convert 1D Array Into 2D Array

class Solution:
    def construct2DArray(self, o: List[int], m: int, n: int) -> List[List[int]]:
        N, x, out = len(o), 0, []
        
        if m*n != N:
            return out
        
        for i in range(m):
            row = []
            for j in range(n):
                row.append(o[x])
                x += 1
            out.append(row)
            
        return out
        

class Solution:
    def construct2DArray(self, o: List[int], m: int, n: int) -> List[List[int]]:
        N, x, out = len(o), 0, []
        
        if m*n != N:
            return out
        
        for i in range(m):
            out.append(o[x:x+n])
            x += n
            
        return out
        