# https://leetcode.com/problems/course-schedule/
# 207. Course Schedule


# Cycle detection usinng DFS (gives TLE)
class Solution:
    def canFinish(self, n: int, pre: List[List[int]]) -> bool:
        adj = [[] for i in range(n)]
        for u, v in pre:
            adj[v].append(u)
        
        visited = [False]*n
        def isCyclic(i):
            if visited[i] == True:
                return True
            
            visited[i] = True
            for nbr in adj[i]:
                if isCyclic(nbr):
                    return True
            visited[i] = False
            
            return False
         
        for i in range(n):
            if isCyclic(i):
                return False
            
        return True


# Cycle detection using DFS with colors - Optimized
class Solution:
    def canFinish(self, n: int, pre: List[List[int]]) -> bool:
        """
        Detect cycle using DFS. Color nodes as per the following:
        White - Node is never visited
        Grey - Node is being visited (i.e. it's adjacent nodes are being visited). If we land on a grey node in our DFS; there's a cycle.
        Black - Node and all it's adjacent vertices are visited.
        """
        # Create adjancency list
        adj = [[] for i in range(n)]
        for u, v in pre:
            adj[v].append(u)

        visited = [False]*n  # Start with all "white"s
        
        def isCyclic(i):
            if visited[i] is None:
                return True
            
            if visited[i] is True:
                return False
            
            visited[i] = None  # Set color of node to "grey"
            for nbr in adj[i]:
                if isCyclic(nbr):
                    return True
                
            visited[i] = True  # Set color of node to "black"
            
            return False
        
        for i in range(n):
            if isCyclic(i):
                return False
            
        return True
            
        