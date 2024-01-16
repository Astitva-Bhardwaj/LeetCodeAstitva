import random

class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.arr.append(val)
        self.map[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        le = self.arr[-1]
        indx = self.map[val]

        if indx != len(self.arr) - 1:
            self.arr[indx] = le
            self.map[le] = indx

        self.arr.pop()
        del self.map[val]

        return True

    def getRandom(self) -> int:
        if not self.arr:
            return -1
        index = random.randint(0, len(self.arr) - 1)
        return self.arr[index]
