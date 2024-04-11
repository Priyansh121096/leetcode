# https://leetcode.com/problems/remove-k-digits

# Solution #1 
# Backtracking gives TLE (22/43)
# Backtracking with caching gives TLE (23/43)
from functools import cache

def set_bit(value, bit):
    return value | (1<<bit)

def clear_bit(value, bit):
    return value & ~(1<<bit)

class Solution:
    @cache
    def minNumber(self, bits: int, k: int):
        if k == self.maxK:
            res, mul = 0, 1
            for i in range(self.N-1, -1, -1):
                if bits & 1 == 1:
                    res += mul*self.num[i]
                    mul *= 10
                bits >>= 1

            return res

        minResult = float("inf")
        for i in range(self.N):
            new_bits = clear_bit(bits, i)
            if new_bits == bits:
                continue

            minResult = min(minResult, self.minNumber(new_bits, k+1))

        return minResult if minResult != float("inf") else 0

    def removeKdigits(self, num: str, k: int) -> str:
        self.num, self.N, self.maxK = [int(x) for x in num], len(num), k
        return str(self.minNumber((2**self.N)-1, 0))
