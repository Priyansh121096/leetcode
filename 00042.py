# https://leetcode.com/problems/trapping-rain-water/
# 42. Trapping Rain Water


# O(3n) time and O(2n) memory
class Solution:
    def trap(self, h: List[int]) -> int:
        N = len(h)
        maxLeft = [0]
        for i in range(1, N):
            maxLeft.append(max(maxLeft[-1], h[i-1]))
            
        maxRight = [0]
        for i in range(N-2, -1, -1):
            maxRight.append(max(maxRight[-1], h[i+1]))
        maxRight = maxRight[::-1]
        
        count = 0
        for i in range(1, N-1):
            count += max(0, min(maxLeft[i], maxRight[i]) - h[i])
            
        return count


# O(2n) time O(n) memory
class Solution:
    def trap(self, h: List[int]) -> int:
        N = len(h)
            
        maxRight = [0]
        for i in range(N-2, -1, -1):
            maxRight.append(max(maxRight[-1], h[i+1]))
        maxRight = maxRight[::-1]
        
        count, maxLeft = 0, h[0]
        for i in range(1, N-1):
            count += max(0, min(maxLeft, maxRight[i]) - h[i])
            maxLeft = max(maxLeft, h[i])
            
        return count
            