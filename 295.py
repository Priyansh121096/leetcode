# https://leetcode.com/problems/find-median-from-data-stream/
# 295. Find Median from Data Stream

from sortedcontainers import SortedList

class MedianFinder:

    def __init__(self):
        self.sl = SortedList()

    def addNum(self, num: int) -> None:
        self.sl.add(num)

    def findMedian(self) -> float:
        N = len(self.sl)
        if N % 2 != 0:
            return self.sl[N//2]
        
        return (self.sl[(N//2)-1] + self.sl[N//2]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Heap based
from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.heaps = [], []
        
    def _balance_heaps(self):
        small, large = self.heaps
        S, L = map(len, self.heaps)
        
        if S > L:
            x = -heappop(small)
            heappush(large, x)
        else:
            x = heappop(large)
            heappush(small, -x)

    def addNum(self, num: int) -> None:
        small, large = self.heaps
        
        if small and num > -small[0]:
            heappush(large, num)
        else:
            heappush(small, -num)
        
        if abs(len(small) - len(large)) > 1:
            self._balance_heaps()

    def findMedian(self) -> float:
        small, large = self.heaps
        S, L = map(len, self.heaps)
        N = S + L
        
        if N % 2 != 0:
            return -small[0] if S > L else large[0]
        
        return (-small[0] + large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()