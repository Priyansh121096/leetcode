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
           
            # If the next building is shorter or of the same height;
            # do nothing.
            if diff <= 0:
                continue
                
            if l == 0:
                # If there are no ladders; use bricks.
                brick_jumps += diff
            elif len(ladder_jumps) < l:
                # If we have some ladders left; use them.
                heappush(ladder_jumps, diff)
            elif diff < ladder_jumps[0]:
                # If the jump is shorter than the shortest jump of ladders;
                # use bricks.
                brick_jumps += diff
            else:
                # If jump is bigger than one of the jumps of ladders; remove the
                # shortest jump from the heap and push this jump into the heap.
                # Use bricks for the removed jump.
                min_ladder_jump = heappop(ladder_jumps)
                brick_jumps += min_ladder_jump
                heappush(ladder_jumps, diff)
                
            # If there are no bricks left; return.
            if brick_jumps > b:
                return i-1
            
        return h-1
