# https://leetcode.com/problems/surrounded-regions/
# 130. Surrounded Regions

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M, N = len(board), len(board[0])

        def dfs(i, j):
            if not (0 <= i < M and 0 <= j < N):
                return
            
            if board[i][j] != 'O':
                return
            
            board[i][j] = 'S'
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
                
        for i in [0, M-1]:
            for j in range(N):
                dfs(i, j)
                
        for i in range(M):
            for j in [0, N-1]:
                dfs(i, j)
                            
        for i in range(M):
            for j in range(N):
                if board[i][j] == 'S':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
                
        return board
            