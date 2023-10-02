# https://leetcode.com/problems/maximum-xor-after-operations/
# 2317. Maximum XOR After Operations

# Key takeways
# 1. AND operation only allows 1 -> 0 but not 0 -> 1.
# 2. When XORing a collection, even number of 1s mean 0 and odd number of 1s mean 1.
# Assume that the operation, num AND (num XOR x) is just num AND y and assume that y 
# can be chosen arbitrarily. This means we can selectively unset any bit (1 -> 0) we want.
# So, if there's zero 1 bits in a column (nth bits of all numbers), the final XOR will have 0 at that col.
# If there's one 1 bit in a col, the final XOR will have 1 at the col.
# If there's more than one 1 bits, we can unset 1 of the bits to make it an odd number and the final XOR will have 1 at the col.
# This is nothing but ORing the entire col since in OR, the col bit is 0 if there's no 1s in the col
# and 1 if there's at least 1 in the col.

from functools import reduce
from operator import ior

class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        return reduce(ior, nums)
