# https://leetcode.com/problems/maximum-units-on-a-truck/
# 1710. Maximum Units on a Truck

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        c = 0
        for i in range(len(boxTypes)):
            nb, nu = boxTypes[i]
            if truckSize >= nb:
                c += nb*nu
                truckSize -= nb
            else:
                c += truckSize*nu
                return c
            
        return c