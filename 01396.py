# https://leetcode.com/problems/design-underground-system/
# 1396. Design Underground System

class UndergroundSystem:
    def __init__(self):
        self.averages = {}
        self.activeTransits = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.activeTransits[id] = (stationName, t)

    def checkOut(self, id: int, endStation: str, endTime: int) -> None:
        startStation, startTime = self.activeTransits.pop(id)
        
        if startStation not in self.averages:
            self.averages[startStation] = {}
            
        if endStation not in self.averages[startStation]:
            self.averages[startStation][endStation] = (0, 0)
          
        newTime = endTime - startTime
        oldCount, oldAvg = self.averages[startStation][endStation]
        newAvg = (oldCount*oldAvg + newTime) / (oldCount + 1)
        
        self.averages[startStation][endStation] = (oldCount+1, newAvg)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.averages[startStation][endStation][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)