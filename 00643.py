# https://leetcode.com/problems/maximum-average-subarray-i

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s, maxAvg = 0, float("-inf")
        for i in range(len(nums)):
            if i < k-1:
                s += nums[i]
            elif i == k-1:
                s += nums[i]
                maxAvg = s/k
            else:
                s = s - nums[i-k] + nums[i]
                maxAvg = max(maxAvg, s/k)

        return maxAvg
