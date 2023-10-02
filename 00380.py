# https://leetcode.com/problems/insert-delete-getrandom-o1/
# 380. Insert Delete GetRandom O(1)

class RandomizedSet:
    def __init__(self):
        self.map = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        
        self.map[val] = len(self.arr)
        self.arr.append(val)
        
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        
        removeIdx = self.map[val]
        lastVal = self.arr[-1]
        
        self.map[lastVal] = removeIdx
        self.arr[removeIdx] = lastVal
        
        self.map.pop(val)
        self.arr.pop()
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()