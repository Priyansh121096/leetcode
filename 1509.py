# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/
# 1509. Minimum Difference Between Largest and Smallest Value in Three Moves

from heapq import nlargest, nsmallest
from typing import List

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0

        smallest = nsmallest(4, nums)
        largest = nlargest(4, nums)[::-1]
        
        return min([l-s for l, s in zip(largest, smallest)])
        