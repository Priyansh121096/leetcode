# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/
# 1524. Number of Sub-arrays With Odd Sum
# Tags: Jumio

# Solution 1 (AC)
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ce, co = 0, 0
        s = 0
        for x in arr:
            if x % 2 == 0:
                ce += 1
            else:
                old_co = co
                co = ce + 1
                ce = old_co
            
            s += co
            
        return s % (10**9+7)
        