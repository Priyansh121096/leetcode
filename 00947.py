# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column
from collections import defaultdict, deque
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        x, y = defaultdict(list), defaultdict(list)
        for i in range(len(stones)):
            a, b = stones[i]
            x[a].append(i)
            y[b].append(i)

        ans = 0
        visited = set()
        for i in range(len(stones)):
            q = deque([i])
            comps = 0

            while q:
                j = q.popleft()
                if j in visited:
                    continue
                visited.add(j)
                comps += 1

                a, b = stones[j]
                for n in x[a]:
                    if n not in visited:
                        q.append(n)

                for n in y[b]:
                    if n not in visited:
                        q.append(n)

            if comps:
                ans += (comps-1)

        return ans
