# https://leetcode.com/problems/reduce-array-size-to-the-half/
# 1338. Reduce Array Size to The Half

from heapq import heapify, heappop
from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        tot_count = len(arr)
        tgt_count = tot_count // 2
        
        c = Counter(arr)
        heap = [(-count, val) for val, count in c.items()]
        heapify(heap)
        
        k = 0
        while tot_count > tgt_count:
            count, val = heappop(heap)
            tot_count -= -count
            k += 1
            
        return k
            