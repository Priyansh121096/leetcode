# https://leetcode.com/problems/meeting-rooms-ii/
# 253. Meeting Rooms II

# Only sorting
class Solution:
    def minMeetingRooms(self, ints: List[List[int]]) -> int:
        N = len(ints)
        starts = sorted((x[0] for x in ints))
        ends = sorted((x[1] for x in ints))
        
        count = 1
        end = 0
        for i in range(1, N):
            if starts[i] < ends[end]:
                count += 1
            else:
                end += 1
                
        return count


# Heap + sorting
from heapq import heapify, heappop

class Solution:
    def minMeetingRooms(self, ints: List[List[int]]) -> int:
        N = len(ints)
        starts = sorted(x[0] for x in ints)
        
        ends = [x[1] for x in ints]
        heapify(ends)
        
        min_end = heappop(ends)
        count = 1
        for i in range(1, N):
            if starts[i] < min_end:
                count += 1
            else:
                min_end = heappop(ends)
                
        return count