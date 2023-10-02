# https://leetcode.com/problems/number-of-ships-in-a-rectangle/
# 1274. Number of Ships in a Rectangle


# Divide and conquer - failing on the following test case
# [[107,938],[883,190]]
# [1000,1000]
# [0,0]

# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
class Sea:
    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
        pass

class Point:
	def __init__(self, x: int, y: int):
		self.x = x
		self.y = y

class ComparablePoint:
    def __init__(self, point: 'Point'):
        self.x = point.x
        self.y = point.y
                
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f"({self.x}, {self.y})"


class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:    
        def helper(bottomLeft, topRight):
            doesHaveShips = sea.hasShips(topRight, bottomLeft)
            if not doesHaveShips:
                return 0
            
            if bottomLeft == topRight:
                return int(doesHaveShips)
            
            width = topRight.x - bottomLeft.x
            height = topRight.y - bottomLeft.y
            
            if width <= 0 or height <= 0:
                return 0
            
            x, y = bottomLeft.x, bottomLeft.y
            
            count = 0
            
            # Bottom left rectangle
            newBottomLeft = ComparablePoint(Point(x, y))
            newTopRight = ComparablePoint(Point(x + (width // 2), y + (height // 2)))
            count += helper(newBottomLeft, newTopRight)
            
            # Bottom right rectangle
            newBottomLeft = ComparablePoint(Point(x + (width // 2) + 1, y))
            newTopRight = ComparablePoint(Point(x + width, y + (height // 2)))
            count += helper(newBottomLeft, newTopRight)
            
            # Top left rectangle
            newBottomLeft = ComparablePoint(Point(x, y + (height // 2) + 1))
            newTopRight = ComparablePoint(Point(x + (width // 2), y + height))
            count += helper(newBottomLeft, newTopRight)
            
            # Top right rectangle
            newBottomLeft = ComparablePoint(Point(x + (width // 2) + 1, y + (height // 2) + 1))
            newTopRight = ComparablePoint(topRight)
            count += helper(newBottomLeft, newTopRight)
            
            return count
            
        return helper(ComparablePoint(bottomLeft), ComparablePoint(topRight))


# Working
# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y
class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:    
        def countInRect(bottomLeft, topRight):
            x1, y1 = bottomLeft.x, bottomLeft.y
            x2, y2 = topRight.x, topRight.y
            
            if x1 > x2 or y1 > y2:
                return 0
            
            doesHaveShips = sea.hasShips(topRight, bottomLeft)
            if not doesHaveShips:
                return 0
            
            if (x1, y1) == (x2, y2):
                return int(doesHaveShips)
            
            xmid, ymid = (x1 + x2) // 2, (y1 + y2) // 2
            
            count = 0
            count += countInRect(Point(x1, y1), Point(xmid, ymid))      # Bottom left rectangle
            count += countInRect(Point(xmid+1, y1), Point(x2, ymid))    # Bottom right rectangle
            count += countInRect(Point(x1, ymid+1), Point(xmid, y2))    # Top left rectangle
            count += countInRect(Point(xmid+1, ymid+1), Point(x2, y2))  # Top right rectangle
            
            return count
            
        return countInRect(bottomLeft, topRight)
