# https://leetcode.com/problems/rotate-image/
# 48. Rotate Image

class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(mat)
        top, bottom, left, right = 0, N-1, 0, N-1
            
        def rotateArray(arr):
            temp = arr[-1]
            for i in range(len(arr)-2, -1, -1):
                arr[i+1] = arr[i]
            arr[0] = temp
            return arr
        
        for i in range(N//2):
            for k in range(right-left):
                mat[top][left+k], mat[top+k][right], mat[bottom][right-k], mat[bottom-k][left] = \
                    rotateArray([mat[top][left+k], 
                                 mat[top+k][right], 
                                 mat[bottom][right-k], 
                                 mat[bottom-k][left],
                                ])
            top += 1
            right -= 1
            bottom -= 1
            left += 1