# https://leetcode.com/problems/k-closest-points-to-origin/
# 973. K Closest Points to Origin

from heapq import nsmallest

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = [(x**2+y**2, i) for i, (x, y) in enumerate(points)]
        kdists = nsmallest(k, dists)
        return [points[i] for dist, i in kdists]