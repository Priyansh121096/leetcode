# Problem: Number of Islands II
# Leetcode 305
# Difficulty: Hard
# Asked at: Google
# LeetCode Link - https://leetcode.com/problems/number-of-islands-ii/

class Solution:
    """
    Problem Statement
    You are given a 2D grid of size m × n. Initially, the grid is all water (0).

    You’re given a list of positions, where each position turns a water cell into land (1).

    Return the number of islands after each operation.

    An island is a group of 1s connected horizontally or vertically.

    Input:
    m = 3, n = 3
    positions = [[0,0], [0,1], [1,2], [2,1], [1,1]]

    Output: [1, 1, 2, 3, 1]

    Time & Space Complexity
    Let:

    P = len(positions)

    N = m × n

    Operation	Complexity
    Each find/union	O(α(N)) amortized
    Each operation	O(1) neighbors × O(α(N))
    Total time	✅ O(P × α(N))
    Space (parent/rank)	✅ O(P)
    Output space	✅ O(P)

    α(N) = inverse Ackermann, practically ≤ 5

    """
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return

        if self.rank[py] > self.rank[px]:
            self.parent[px] = py
        elif self.rank[py] < self.rank[px]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        self.count -= 1

    def numberOfIslands2(self, m: int, n: int, positions: list[tuple[int, int]]) -> list[int]:
        id_ = lambda i, j: n*i + j
        self.parent = {}
        self.rank = {}
        self.count = 0
        answers = []

        for i, j in positions:
            iid = id_(i, j)
            self.parent[iid] = iid
            self.rank[iid] = 0
            self.count += 1

            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i+x, j+y
                niid = id_(ni, nj)
                if not 0 <= niid < m*n:
                    continue
                if niid not in self.parent:
                    continue
                print(i, j, ni, nj, self.count, self.parent)
                self.union(iid, niid)
                print(i, j, ni, nj, self.count, self.parent)

            answers.append(self.count)

        return answers
