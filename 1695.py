# https://leetcode.com/problems/maximum-erasure-value/
# 1695. Maximum Erasure Value

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        currSum, maxSum = nums[0], nums[0]
        visited = set([nums[0]])
        
        for right in range(1, len(nums)):
            while nums[right] in visited:
                currSum -= nums[left]
                visited.remove(nums[left])
                left += 1
            
            visited.add(nums[right])
            currSum += nums[right]
            maxSum = max(currSum, maxSum)
            
        return maxSum
        