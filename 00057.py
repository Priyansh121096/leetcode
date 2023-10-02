# https://leetcode.com/problems/insert-interval/
# 57. Insert Interval

class Solution:
    def insert(self, ints: List[List[int]], ni: List[int]) -> List[List[int]]:
        N = len(ints)
        
        # If there's no existing interval; ni will be the only interval in the o/p.
        if N == 0:
            return [ni]
        
        x, y = ni
        is_done = False  # Whether ni has been merged.
        
        # If ni lies to the left of the start of ints; insert it at the beginning and return.
        if y < ints[0][0]:
            ints.insert(0, ni)
            return ints
        
        out = [ints[0]]
        for i in range(1, N):
            preva, prevb = out.pop()
            curra, currb = ints[i]
            
            if not is_done and curra > x:
                # If the current interval is on ni's right; merge ni with the previous interval
                # if possible.
                if prevb < x:
                    out.extend([[preva, prevb], ni])
                else:
                    out.append([min(preva, x), max([prevb, y])])
                is_done = True
                preva, prevb = out.pop()
                
            if prevb >= curra:
                # If the previous interval's end is after the current interval's start; merge them.
                out.append([min(preva, curra), max([prevb, currb])])
            else:
                # Else, put them as two separate intervals.
                out.extend([[preva, prevb], [curra, currb]])
                
        if not is_done:
            preva, prevb = out.pop()
            if prevb < x:
                out.extend([[preva, prevb], ni])
            else:
                out.append([min(preva, x), max([prevb, y])])
                
        return out

# Simpler
class Solution:
    def insert(self, ints: List[List[int]], ni: List[int]) -> List[List[int]]:
        N = len(ints)
        out = []
        
        for i in range(N):
            x, y = ni
            a, b = ints[i]
            
            # If the new interval is on the left of the current interval;
            # put it in the output and put the entire remaining interval list
            # also in the output and return.
            if y < a:
                out.append(ni)
                out += ints[i:]
                return out
            
            # If the new interval is to the right of the current interval; 
            # put the current interval in the output.
            if b < x:
                out.append(ints[i])
                continue
                
            # Merge the two intervals and consider the merged interval as the 
            # interval to be inserted in the next iteration.
            ni = [min(a, x), max(b, y)]
            
        out.append(ni)
        
        return out
