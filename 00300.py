# https://leetcode.com/problems/longest-increasing-subsequence/
# 300. Longest Increasing Subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return max(dp)

# Binary search based LIS
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        tails = [nums[0]]
        for i in range(1, N):
            num = nums[i]
            if num > tails[-1]:
                tails.append(num)
            elif num < tails[0]:
                tails[0] = num
            else:
                idx = bisect_left(tails, num)
                tails[idx] = num
                    
        return len(tails)
        