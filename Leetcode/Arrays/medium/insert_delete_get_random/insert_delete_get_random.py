

import random

class RandomizedSet:

    def __init__(self):
        self.arr = set([])
        self.len = 0

    def insert(self, val: int) -> bool:
        self.arr.add(val)
        self.arr = set(self.arr)
        if len(self.arr) != self.len:
            self.len+=1
            return True
        return False

    def remove(self, val: int) -> bool:
        self.arr.discard(val)
        if len(self.arr) != self.len:
            self.len-=1
            return True
        return False

    def getRandom(self) -> int:
        arr = list(self.arr)
        ran = random.randint(0, self.len-1)
        return arr[ran]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()