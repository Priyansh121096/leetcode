# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # Targets can only be one of these two
        # (btw there's nothing special about the first index)
        t1, t2 = tops[0], bottoms[0]

        # ct1, ct2 -> flips required to make top row equal to t1 and t2 respectively
        # cb1, cb2 -> flips required to make bottom row equal to t1 and t2 respectively
        # impossible_t1, impossible_t2 -> whether making any one row equal to t1 and t2
        # respectively is impossible
        ct1, cb1, impossible_t1 = 0, 0, False
        ct2, cb2, impossible_t2 = 0, 0, False
        for i in range(len(tops)):
            t, b = tops[i], bottoms[i]
            
            if t == t1 and b == t1:
                pass
            elif t == t1 and not b == t1:
                cb1 += 1
            elif not t == t1 and b == t1:
                ct1 += 1
            else:
                impossible_t1 = True

            if t == t2 and b == t2:
                pass
            elif t == t2 and not b == t2:
                cb2 += 1
            elif not t == t2 and b == t2:
                ct2 += 1
            else:
                impossible_t2 = True
    
        if impossible_t1 and impossible_t2:
            return -1

        if impossible_t1:
            return min(ct2, cb2)

        if impossible_t2:
            return min(ct1, cb1)
        
        return min(ct1, cb1, ct2, cb2)
        
