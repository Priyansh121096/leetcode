# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
# 1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts

class Solution:
    def maxArea(self, h: int, w: int, hcs: List[int], vcs: List[int]) -> int:
        hcs, vcs = sorted(hcs), sorted(vcs)
        hcs.append(h)
        vcs.append(w)
        
        mhc, phc = -inf, 0
        for hc in hcs:
            mhc = max(mhc, hc - phc)
            phc = hc
            
        mvc, pvc = -inf, 0
        for vc in vcs:
            mvc = max(mvc, vc - pvc)
            pvc = vc

        return (mhc*mvc) % (10**9 + 7)