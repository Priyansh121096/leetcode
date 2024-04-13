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


# Solution #2
# Simpler recursion - gives TLE (23/43)
from functools import cache

class Solution:
    @cache
    def removeOne(self, num):
        num = [int(x) for x in num]
        minRes = float("inf")
        for i in range(len(num)):
            res = 0
            for j in range(len(num)):
                if i == j:
                    continue
                res = res*10 + num[j]
            minRes = min(minRes, res)
        return str(minRes)

    def removeKdigits(self, num: str, k: int) -> str:
        if k == 1:
            return self.removeOne(num)

        new_num = self.removeOne(num[:len(num)-k+1])
        return self.removeKdigits(f"{new_num}{num[len(num)-k+1:]}", k-1)

# Solution #3
# Same as #1 but with bit manipulation
import sys

sys.set_int_max_str_digits(2*(10**5))

def reset_last_n_bits(bits, n):
    mask = (2**(10**5) - 1) << n
    return bits & mask

def set_last_n_bits(bits, n):
    mask = (2**(n) - 1)
    return bits | mask

def reset_last_nth_bit(bits, n):
    return bits & ~(1<<n)

def p(bits: int):
    print(f"{bits:b}")

class Solution:
    def removeOne(self, bits: int):
        N = len(self.num)
        minRes, minBits = float("inf"), None
        
        for i in range(N):
            curr_bit = (bits >> (N-i-1)) & 1
            if not curr_bit:
                continue

            res, mul = 0, 1
            new_bits = reset_last_nth_bit(bits, N-i-1)
            new_bits_copy = new_bits
            for j in range(N-1, -1, -1):
                if new_bits & 1 == 1:
                    res += mul*self.num[j]
                    mul *= 10

                new_bits >>= 1

            if res < minRes:
                minRes, minBits = res, new_bits_copy

        return minBits if minRes != float("inf") else 0

    def removeKdigitsHelper(self, bits: int, k: int) -> str:
        # print("rkdh start")
        p(bits)
        print(k)
        if k == 1:
            return self.removeOne(bits)

        new_bits = self.removeOne(reset_last_n_bits(bits, k-1))
        # print("rkdh mid")
        p(new_bits)

        return self.removeKdigitsHelper(set_last_n_bits(new_bits, k-1), k-1)

    def removeKdigits(self, num: str, k: int) -> str:
        N = len(num)
        self.num = [int(x) for x in num]
        
        final_bits = self.removeKdigitsHelper(((2**N)-1), k)
        p(final_bits)
        
        res, mul = 0, 1
        for i in range(N-1, -1, -1):
            if (final_bits & 1) == 1:
                res += mul*self.num[i]
                mul *= 10
            final_bits >>= 1

        return str(res)

# Solution #4 
# Min heap - passes all test cases
# O(Nlogk) time - O(k) space
import sys
from heapq import heappop, heappush

sys.set_int_max_str_digits(10**5)

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        N = len(num)
        if N == k: return "0"
        
        result, li, heap = [], -1, []
        for i in range(len(num)):
            heappush(heap, (int(num[i]), i))
            
            # print("Before pop")
            # print(heap, li, result)
            if i == len(result)+k:
                minNum, minI = heappop(heap)
                while minI <= li:
                    minNum, minI = heappop(heap)
                result.append(str(minNum))
                li = minI
            # print("After pop")
            # print(heap, li, result)

        return str(int("".join(result)))
