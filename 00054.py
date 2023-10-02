# https://leetcode.com/problems/spiral-matrix/
# 54. Spiral Matrix

import math

class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        k, out = 0, []
        v = [[False for j in range(n)] for i in range(m)]
        for k in range(math.ceil(min(m, n)/2)):
            # i=0+k; j=(k, n-1-k)
            i = k
            for j in range(k, n-k):
                if not v[i][j]:
                    out.append(mat[i][j])
                    v[i][j] = True
            
            # j=n-k-1; i=(k, m-1-k)
            j = n-k-1
            for i in range(k, m-k):
                if not v[i][j]:
                    out.append(mat[i][j])
                    v[i][j] = True
            
            # i=m-1-k; j=(n-1-k, 0+k)
            i = m-1-k
            for j in range(n-1-k, k-1, -1):
                if not v[i][j]:
                    out.append(mat[i][j])
                    v[i][j] = True
            
            # j=0+k; i=(m-1-k, 0+k)
            j = k
            for i in range(m-1-k, k-1, -1):
                if not v[i][j]:
                    out.append(mat[i][j])
                    v[i][j] = True
                    
        return out


class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        out = []
        top, bottom, left, right = 0, m-1, 0, n-1
        
        def shouldBreak():
            return top > bottom or left > right
        
        while True:
            for j in range(left, right+1):
                out.append(mat[top][j])
            top += 1
            if shouldBreak(): break
            
            for i in range(top, bottom+1):
                out.append(mat[i][right])
            right -= 1
            if shouldBreak(): break
            
            for j in range(right, left-1, -1):
                out.append(mat[bottom][j])
            bottom -= 1
            if shouldBreak(): break
            
            for i in range(bottom, top-1, -1):
                out.append(mat[i][left])
            left += 1
            if shouldBreak(): break
            
            
        return out