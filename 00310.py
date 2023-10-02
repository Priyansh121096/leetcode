# https://leetcode.com/problems/minimum-height-trees/
# 310. Minimum Height Trees

# Toplogical sort - start BFS with leaves (1-degree nodes) and keep removing edges. 
# If new nodes become leaves, add them to the BFS queue until 1 or 2 nodes are left.
# The left nodes are the roots of Minimum Height Trees.
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [set() for i in range(n)]
        leaves = {i for i in range(n)}
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
            
            if u in leaves and len(adj[u]) > 1:
                leaves.remove(u)
            if v in leaves and len(adj[v]) > 1:
                leaves.remove(v)
                
        nodes_left = n
        while nodes_left > 2:
            nodes_left -= len(leaves)
            
            new_leaves = []
            for leaf in leaves:
                node = adj[leaf].pop()
                adj[node].remove(leaf)
                
                if len(adj[node]) == 1:
                    new_leaves.append(node)
                    
            leaves = new_leaves
            
        return leaves