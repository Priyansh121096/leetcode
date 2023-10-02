# https://leetcode.com/problems/meeting-rooms/
# 252. Meeting Rooms

class Solution:
    def canAttendMeetings(self, ints: List[List[int]]) -> bool:
        ints = sorted(ints, key=lambda x: x[0])
        
        for i in range(1, len(ints)):
            if ints[i][0] < ints[i-1][1]:
                return False
            
        return True