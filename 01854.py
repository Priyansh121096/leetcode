# https://leetcode.com/problems/maximum-population-year/
# 1854. Maximum Population Year

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        maxP, maxY = -inf, None
        minYear, maxYear = inf, -inf
        pop = defaultdict(int)
        
        for birth, death in logs:
            pop[birth] += 1
            minYear = min(minYear, birth)
            pop[death] -= 1
            maxYear = max(maxYear, death)
        
        for year in range(minYear, maxYear+1):
            pop[year] += pop[year-1]
            
            if pop[year] > maxP:
                maxP = pop[year]
                maxY = year
            
        return maxY
        
        