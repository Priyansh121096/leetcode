# https://leetcode.com/problems/amount-of-new-area-painted-each-day/
# 2158. Amount of New Area Painted Each Day

# TLE
class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        x = min((x[0] for x in paint))
        y = max((x[1] for x in paint))
        
        arr = [1]*(y-x)
        out = []
        for i, j in paint:
            np = 0
            for k in range(i-x, j-x):
                np += arr[k]
                arr[k] = 0
            out.append(np)
            
        return out