# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
# 1293. Shortest Path in a Grid with Obstacles Elimination

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        M, N = len(grid), len(grid[0])
                
        q = [(0, 0, k)]
        visited = set()
        steps = 0
        while q:
            newq = []
            for i, j, k in q:
                # If it's the last cell; return the number of steps.
                if i == M-1 and j == N-1:
                    return steps

                # If the cell is already visited; do nothing.
                if (i, j, k) in visited:
                    continue

                # Mark the cell as visited.
                visited.add((i, j, k))

                # Right
                if j < N-1:
                    if grid[i][j+1] == 0:
                        newq.append((i, j+1, k))
                    elif k > 0:
                        newq.append((i, j+1, k-1))

                # Down
                if i < M-1:
                    if grid[i+1][j] == 0:
                        newq.append((i+1, j, k))
                    elif k > 0:
                        newq.append((i+1, j, k-1))
                        
                # Left
                if j > 0:
                    if grid[i][j-1] == 0:
                        newq.append((i, j-1, k))
                    elif k > 0:
                        newq.append((i, j-1, k-1))

                # Up
                if i > 0:
                    if grid[i-1][j] == 0:
                        newq.append((i-1, j, k))
                    elif k > 0:
                        newq.append((i-1, j, k-1))

            q = newq
            steps += 1
            
        return -1