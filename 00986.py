# https://leetcode.com/problems/interval-list-intersections/
# 986. Interval List Intersections

class Solution:
    def intervalIntersection(self, fl: List[List[int]], sl: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        out = []
        while i < len(fl) and j < len(sl):
            si, ei = fl[i]
            sj, ej = sl[j]
            
            if ei < sj:
                i += 1
            elif ej < si:
                j += 1
            elif si >= sj and ei <= ej:
                out.append([si, ei])
                i += 1
            elif sj >= si and ej <= ei:
                out.append([sj, ej])
                j += 1
            elif si <= sj and ei <= ej:
                out.append([sj, ei])
                i += 1
            elif sj <= si and ej <= ei:
                out.append([si, ej])
                j += 1
                
        return out
    
# Simpler
class Solution:
    def intervalIntersection(self, fl: List[List[int]], sl: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        out = []
        while i < len(fl) and j < len(sl):
            si, ei = fl[i]
            sj, ej = sl[j]
            
            # Keep the interval which starts before the other as "i" and the other as "j".
            switched = False
            if si > sj:
                si, ei, sj, ej = sj, ej, si, ei
                i, j = j, i
                switched = True
            
            if ei < sj:
                # If i ends before j's start, there's no intersection.
                i += 1
            elif ei >= ej:
                # If i ends after j's end, entire j is the intersection.
                out.append([sj, ej])
                j += 1
            else:
                # If i ends before j's end, [sj, ei] is the intersection.
                out.append([sj, ei])
                i += 1
                
            # If we had switched the intervals before; switch the i and j pointers
            if switched:
                i, j = j, i

        return out


# Ideal solution
class Solution:
    def intervalIntersection(self, fl: List[List[int]], sl: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        out = []
        while i < len(fl) and j < len(sl):
            si, ei = fl[i]
            sj, ej = sl[j]
            
            # Criss-cross lock condition
            # Start of both intervals should be less than the ends of the other intervals.
            if si <= ej and sj <= ei:
                out.append([max(si, sj), min(ei, ej)])
                
            if ei <= ej:
                i += 1
            else:
                j += 1

        return out
                