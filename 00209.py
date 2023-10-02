# https://leetcode.com/problems/minimum-size-subarray-sum/
# 209. Minimum Size Subarray Sum

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, currSum, minL = 0, nums[0], inf if nums[0] < target else 1
        for right in range(1, len(nums)):
            currSum += nums[right]
                
            while left <= right and currSum >= target:
                if currSum >= target:
                    minL = min(minL, right-left+1)
                currSum -= nums[left]
                left += 1
                     
        return minL if minL != inf else 0