# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
# 323. Number of Connected Components in an Undirected Graph

# Union-Find
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        
        def find(x):
            return x if parent[x] == x else find(parent[x])
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            parent[py] = px
            
        [union(x, y) for x, y in edges]
        
        reps = set()
        for i in range(n):
            reps.add(find(i))
            
        return len(reps)

# Union-find with path compression and rank.
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent, rank = list(range(n)), [0]*n
        
        def find(x):
            # Find with path compression
            if x != parent[x]:
                parent[x] = find(parent[x])
            
            return parent[x]
        
        def union(x, y):
            # Union by rank
            px, py = find(x), find(y)
            if px != py:
                if rank[px] > rank[py]:
                    parent[py] = px
                elif rank[px] < rank[py]:
                    parent[px] = py
                else:
                    parent[py] = px
                    rank[px] += 1
            
        [union(x, y) for x, y in edges]
        
        return len({find(x) for x in parent})
        
        