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


class Solution:
    def criticalConnections(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        edges = set(map(tuple, (map(sorted, edges))))
        rank = [-2] * n

        def dfs(node, depth):
            if rank[node] >= 0:
                # visiting (0<=rank<n), or visited (rank=n)
                return rank[node]

            rank[node] = depth

            min_back_depth = n
            for neighbor in graph[node]:
                if rank[neighbor] == depth - 1:
                    continue  # don't immmediately go back to parent. that's why i didn't choose -1 as the special value, in case depth==0.

                # Find the minimum depth a neighbor can reach
                back_depth = dfs(neighbor, depth + 1)

                # If a neighbor can lead back to an ancestor of current node
                # (or the node itself not via the node-neighbor edge),
                # then the node-neighbor is not critical
                if back_depth <= depth:
                    edges.discard(tuple(sorted((node, neighbor))))

                min_back_depth = min(min_back_depth, back_depth)

            return min_back_depth

        dfs(0, 0)  # since this is a connected graph, we don't have to loop over all nodes.
        return list(edges)
