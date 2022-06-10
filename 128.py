# https://leetcode.com/problems/longest-consecutive-sequence/
# 128. Longest Consecutive Sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) in (0, 1):
            return len(nums)
        
        nums = set(nums)
        lcs = 0
        for start in nums:
            if start-1 not in nums:
                end = start+1
                while end in nums:
                    end += 1
                lcs = max(lcs, end-start)
                
        return lcs
