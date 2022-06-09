# https://leetcode.com/problems/find-the-duplicate-number/
# 287. Find the Duplicate Number

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sp = fp = nums[0]
        while True:
            sp = nums[sp]
            fp = nums[nums[fp]]
            if sp == fp:
                break
                
        entry = nums[0]
        while entry != sp:
            entry = nums[entry]
            sp = nums[sp]
            
        return entry
            