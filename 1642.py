# https://leetcode.com/problems/furthest-building-you-can-reach/
# 1642. Furthest Building You Can Reach

from heapq import heappush, heappop

class Solution:
    def furthestBuilding(self, hts: List[int], b: int, l: int) -> int:
        h = len(hts)
        
        ladder_jumps = []
        brick_jumps = 0
        for i in range(1, h):
            diff = hts[i] - hts[i-1]
            
            if diff <= 0:
                continue
                
            if len(ladder_jumps) < l:
                heappush(ladder_jumps, diff)
            elif l == 0:
                brick_jumps += diff
            elif diff < ladder_jumps[0]:
                brick_jumps += diff
            else:
                min_ladder_jump = heappop(ladder_jumps)
                brick_jumps += min_ladder_jump
                heappush(ladder_jumps, diff)
                
            if brick_jumps > b:
                return i-1
            
        return h-1
                
                