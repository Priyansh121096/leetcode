# https://leetcode.com/problems/critical-connections-in-a-network
from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        disc = [None for _ in range(n)]
        low = [None for _ in range(n)]
        bridges = []
        
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        self.dfs(0, None, 0, disc, low, bridges, adj)

        return bridges

    def dfs(self, u, parent, time, disc, low, bridges, adj):
        disc[u] = low[u] = time
        for v in adj[u]:
            if v == parent: continue
            if disc[v] is None:  # unvisited
                self.dfs(v, u, time+1, disc, low, bridges, adj)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    bridges.append([u, v])
            else:
                low[u] = min(low[u], disc[v])
