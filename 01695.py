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
        

# Avoid doing a lot of membership checks in the visited set.   
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        currSum, maxSum = nums[0], nums[0]
        visited = set([nums[0]])
        
        for right in range(1, len(nums)):
			# Note: Instead of if + while below, we could also simply do
			# `while nums[right] in visited` and it'll help save the double nesting
			# as well as the duplicate 3 lines after while. But I've found it to be
			# slowing down the code because of the repeated set lookups.
			# Compare https://leetcode.com/submissions/detail/720467663/ and
			# https://leetcode.com/submissions/detail/720466011/.
            if nums[right] in visited:
                while nums[right] != nums[left]:
                    currSum -= nums[left]
                    visited.remove(nums[left])
                    left += 1
                currSum -= nums[left]
                visited.remove(nums[left])
                left += 1
                
            visited.add(nums[right])
            currSum += nums[right]
            maxSum = max(currSum, maxSum)
            
        return maxSum
        