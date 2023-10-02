# https://leetcode.com/problems/count-subarrays-with-score-less-than-k/
# 2302. Count Subarrays With Score Less Than K

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left, currSum = 0, nums[0]
        count = 1 if nums[0] < k else 0
        
        for right in range(1, len(nums)):
            # Shrink the sliding window till we get a subarray 
            # whose score is less than k.
            currSum += nums[right]
            while currSum * (right-left+1) >= k:
                currSum -= nums[left]
                left += 1

            # Add all new subarrays ending at right.
            count += (right-left+1)

        return count
