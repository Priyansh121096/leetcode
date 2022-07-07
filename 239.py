# https://leetcode.com/problems/sliding-window-maximum/
# 239. Sliding Window Maximum

# Solution 1 (AC) - Had to see solution from discuss
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1 or k == 1:
            return nums
        
        queue, out = deque([]), []
        for i in range(len(nums)):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            
            if i-k == queue[0]:
                queue.popleft()
            
            if i >= k-1:
                out.append(nums[queue[0]])
                
        return out
