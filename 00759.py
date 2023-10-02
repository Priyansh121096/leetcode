# https://leetcode.com/problems/employee-free-time/
# 759. Employee Free Time


# Sweep-line algorithm - https://www.youtube.com/watch?v=m13Omjv43eM
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        points = []
        for emp in schedule:
            for interval in emp:
                points.append((interval.start, 0))
                points.append((interval.end, 1))
                    
        points = sorted(points, key=lambda x: (x[0], x[1]))
        
        count = 1
        ints = []
        for i in range(1, len(points)):
            point, is_end = points[i]
            
            if count == 0:
                ints.append(Interval(points[i-1][0], point))
            
            if is_end:
                count -= 1
            else:
                count += 1
        
        return ints