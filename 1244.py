# https://leetcode.com/problems/design-a-leaderboard/
# 1244. Design A Leaderboard

from collections import defaultdict
from heapq import nlargest

class Leaderboard2:

    def __init__(self):
        self.scores = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] += score

    def top(self, K: int) -> int:
        return sum(nlargest(K, self.scores.values()))

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)

from collections import defaultdict
from sortedcollections import ValueSortedDict

class Leaderboard:

    def __init__(self):
        self.sorted_scores = ValueSortedDict(lambda val: -val)

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.sorted_scores:
            self.sorted_scores[playerId] = 0
        self.sorted_scores[playerId] += score

    def top(self, K: int) -> int:
        print(self.sorted_scores)
        return sum(list(self.sorted_scores.values())[:K])

    def reset(self, playerId: int) -> None:
        self.sorted_scores[playerId] = 0

obj = Leaderboard()
obj.addScore(0, 5)
param_2 = obj.top(1)
obj.reset(0)