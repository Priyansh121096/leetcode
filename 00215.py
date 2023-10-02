# https://leetcode.com/problems/kth-largest-element-in-an-array/
# 215. Kth Largest Element in an Array

from heapq import nlargest

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return nlargest(k, nums)[-1]