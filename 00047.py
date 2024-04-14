# https://leetcode.com/problems/permutations-ii

class Solution:
    def helper(self, nums, perm):
        if not nums:
            self.all_.add(tuple(perm))
            return

        prev = None
        for i in range(len(nums)):
            curr = nums[i]
            if prev == curr:
                continue

            perm.append(curr)
            new_nums = nums[:i] + nums[i+1:]
            self.helper(new_nums, perm)
            perm.pop()

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.all_ = set()
        self.helper(nums, [])
        return self.all_


# Optimal
from collections import Counter

class Solution:
    def helper(self, perm, counts):
        if len(perm) == self.N:
            self.all_.append(perm[:])
            return

        for x in counts:
            if counts[x]:
                perm.append(x)
                counts[x] -= 1
                self.helper(perm, counts)
                counts[x] += 1
                perm.pop()

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.all_, self.N = [], len(nums)
        self.helper([], Counter(nums)) 
        return self.all_
