# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
# 1347. Minimum Number of Steps to Make Two Strings Anagram

from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cs = Counter(s)
        for l in t:
            if l in cs:
                cs[l] -= 1
                if cs[l] == 0:
                    del cs[l]
        
        return sum(cs.values())