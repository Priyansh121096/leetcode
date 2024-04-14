# https://leetcode.com/problems/permutations/
# 46. Permutations

class Solution:
    def helper(self, perm, rem):
        if not rem:
            self.all_.append(perm[:])
            return

        for x in rem:
            perm.append(x)
            rem.remove(x)
            self.helper(perm, set(rem))
            rem.add(x)
            perm.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.all_ = []
        self.helper([], set(nums))
        return self.all_
