# https://leetcode.com/problems/my-calendar-i/
# 729. My Calendar I

from sortedcontainers import SortedList
from bisect import bisect_left

class MyCalendar:

    def __init__(self):
        self.sl = SortedList([])

    def book(self, start: int, end: int) -> bool:
        idx = bisect_left(self.sl, (start, end))
        prev, curr = self.sl[idx-1] if idx != 0 else None, self.sl[idx] if idx != len(self.sl) else None
        
        if prev and (prev[1] > start):
            return False
        
        if curr and (curr[0] < end):
            return False
        
        self.sl.add((start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)