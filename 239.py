# https://leetcode.com/problems/sliding-window-maximum/
# 239. Sliding Window Maximum

# Solution 1 (AC) - Had to see solution from discuss
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1 or k == 1:
            return nums
        
        q, arr = deque([]), []
        for i in range(len(nums)):
            #print(i, nums[i], q, arr)
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            
            if i-k == q[0]:
                q.popleft()
            
            if i >= k-1:
                arr.append(nums[q[0]])
                
        return arr
        
                
            