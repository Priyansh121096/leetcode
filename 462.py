# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
# 462. Minimum Moves to Equal Array Elements II

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        N = len(nums)
        nums = sorted(nums)
        tgt = nums[N//2] if N % 2 != 0 else (nums[(N-1)//2] + nums[N//2]) // 2
        c = 0
        for num in nums:
            c += abs(num - tgt)
            
        return c