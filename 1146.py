# https://leetcode.com/problems/snapshot-array/
# 1146. Snapshot Array
from bisect import bisect_right

class SnapshotArray:
    def __init__(self, length: int):
        self.arr = [[[0, 0]] for _ in range(length)]
        self.is_snap_called = [False]*length  # Should we snap this column on the next `set`?
        self.snap_id = 0  # Max snap_id right now
        
    def set(self, index: int, val: int) -> None:
        if self.is_snap_called[index]:
            self.arr[index].append([self.snap_id, val])
            self.is_snap_called[index] = False
        else:
            self.arr[index][-1][1] = val
        
    def snap(self) -> int:
        self.is_snap_called = [True]*len(self.is_snap_called)
        self.snap_id += 1
        return self.snap_id-1

    def get(self, index: int, snap_id: int) -> int:
        if snap_id == 0:
            return self.arr[index][0][1]
        elif snap_id >= self.snap_id:
            print(index, snap_id, self.snap_id, self.arr[index])
            return self.arr[index][-1][1]
        else:
            idx = bisect_right(self.arr[index], [snap_id, -inf])
            idx = idx if (idx < len(self.arr[index]) and self.arr[index][idx][0] == snap_id) else idx-1
            return self.arr[index][idx][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)