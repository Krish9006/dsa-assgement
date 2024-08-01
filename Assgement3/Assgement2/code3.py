from random import choice

class RandomizedSet:
    def __init__(self):
        self.set = set()
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        self.set.add(val)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.set:
            return False
        self.set.remove(val)
        self.list.remove(val)
        return True

    def getRandom(self) -> int:
        return choice(self.list)