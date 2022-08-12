# https://leetcode.com/problems/course-schedule-iii/
# 630. Course Schedule III

from heapq import heappush, heapreplace

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = sorted(courses, key=lambda x: x[1])
        totalTimeConsumed = 0
        heap = []
        for currentDuration, currentLastDay in courses:
            if totalTimeConsumed + currentDuration <= currentLastDay:
                totalTimeConsumed += currentDuration
                heappush(heap, -currentDuration)
            else:
                if heap and currentDuration < -heap[0]:
                    prevMaxDuration = -heapreplace(heap, -currentDuration)
                    totalTimeConsumed = totalTimeConsumed - prevMaxDuration + currentDuration
                
        return len(heap)