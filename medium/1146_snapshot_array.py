class SnapshotArray:
    def __init__(self, length: int):
        self.arr = [0]*length
        print(self.arr)

    def set(self, index: int, val: int):
        self.arr[index] = val

    def snap(self) -> int:
        return self.arr

    # def get(self, index: int, snap_id: int) -> int:
    #     return 5


# Your SnapshotArray object will be instantiated and called as such:
length = 3
index = 0
val = 5
obj = SnapshotArray(length)
obj.set(index, val)
param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
