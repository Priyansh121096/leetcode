# https://leetcode.com/problems/merge-intervals/
# 56. Merge Intervals

class Solution:
    def merge(self, ints: List[List[int]]) -> List[List[int]]:
        N = len(ints)
        if N <= 1:
            return ints
        
        # Sort based on starts
        ints = sorted(ints, key=lambda x: x[0])
        
        mints = [ints[0]]
        for i in range(1, N):
            # See if the last interval in the output so far can be merged with
            # the current interval.
            prev, curr = mints.pop(), ints[i]
            
            if prev[1] >= curr[0]:
                newint = [prev[0], max(curr[1], prev[1])]
                mints.append(newint)
                continue
                
            mints.extend([prev, curr])
            
        return mints