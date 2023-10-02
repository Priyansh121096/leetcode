# https://leetcode.com/problems/course-schedule-ii/
# 210. Course Schedule II


# Topological sort using BFS - Kahn's algorithm
from collections import deque

class Solution:
    def findOrder(self, N: int, pre: List[List[int]]) -> List[int]:
        in_deg = [0 for _ in range(N)]
        adj = [[] for _ in range(N)]
        starts = {i for i in range(N)}
        for v, u in pre:
            in_deg[v] += 1
            adj[u].append(v)
            try:
                starts.remove(v)
            except KeyError:
                pass
        
        queue = deque(starts)
        topo = []
        while queue:
            u = queue.popleft()
            topo.append(u)
            
            for v in adj[u]:
                in_deg[v] -= 1
                if in_deg[v] == 0:
                    queue.append(v)
                    
        for u in range(N):
            if in_deg[u] != 0:
                return []
        
        return topo
            