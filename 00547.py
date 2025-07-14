# https://leetcode.com/problems/number-of-provinces
from collections import defaultdict, deque

class Solution:
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return
        
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1

    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        N = len(isConnected)
        self.parent = list(range(N))
        self.rank = [0] * N

        for i in range(N):
            for j in range(N):
                if isConnected[i][j]:
                    self.union(i, j)

        provinces = defaultdict(int)
        for i in range(N):
            pi = self.find(i)
            provinces[pi] += 1

        return len(provinces)

        
