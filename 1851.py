# https://leetcode.com/problems/minimum-interval-to-include-each-query/
# 1851. Minimum Interval to Include Each Query

from heapq import heappush, heappop

class Solution:
    def minInterval(self, ints: List[List[int]], qrs: List[int]) -> List[int]:
        ints = sorted(ints)
        sqrs = sorted(range(len(qrs)), key=lambda idx: qrs[idx])
        ans = [None]*len(qrs)
        
        heap = []
        intIdx = 0
        for qidx in sqrs:
            q = qrs[qidx]
                
            while intIdx < len(ints) and ints[intIdx][0] <= q:
                left, right = ints[intIdx]
                size = right - left + 1
                heappush(heap, (size, right))
                intIdx += 1
                
            while heap and heap[0][1] < q:
                heappop(heap)
                
            ans[qidx] = heap[0][0] if heap else -1
            
        return ans
        