# https://leetcode.com/problems/maximum-subarray/
# 53. Maximum Subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum, maxSum = nums[0], nums[0]
        for i in range(1, len(nums)):
            if currSum + nums[i] < nums[i]:
                currSum = nums[i]
            else:
                currSum += nums[i]
                
            maxSum = max(currSum, maxSum)
            
        return maxSum