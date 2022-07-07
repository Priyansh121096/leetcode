# https://leetcode.com/problems/container-with-most-water/
# 11. Container With Most Water

class Solution:
    def maxArea(self, h: List[int]) -> int:
        N = len(h)
        
        left, right = 0, N-1
        maxArea = 0
        
        while left < right:
            area = (right-left)*min(h[left], h[right])
            maxArea = max(maxArea, area)
            if h[left] <= h[right]:
                left += 1
            else:
                right -= 1
                
        return maxArea
