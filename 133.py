# https://leetcode.com/problems/clone-graph/
# 133. Clone Graph

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# Reconstruct edges using BFS and construct new graph.
from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        
        visited = set()
        queue = deque([node])
        N = 0
        edges = []
        while queue:
            curr = queue.popleft()
            visited.add(curr.val)
            N += 1
            
            for ngh in curr.neighbors:
                if ngh.val not in visited:
                    edges.append((curr.val, ngh.val))
                    queue.append(ngh)
                    
        nodes = [Node(i+1) for i in range(N)]
        for u, v in edges:
            nodes[u-1].neighbors.append(nodes[v-1])
            nodes[v-1].neighbors.append(nodes[u-1])
            
        return nodes[0]


# Recursion
class Solution:    
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        
        new_nodes = {}
        def dfs(curr):
            if curr.val in new_nodes:
                return 
            
            clone = Node(curr.val)
            new_nodes[curr.val] = clone
            
            for ngh in curr.neighbors:
                if ngh.val not in new_nodes:
                    dfs(ngh)
            
            clone.neighbors = [new_nodes[x.val] for x in curr.neighbors]
            
        dfs(node)
                
        return new_nodes[1]