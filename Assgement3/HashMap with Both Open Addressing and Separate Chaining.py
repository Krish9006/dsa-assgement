class HashMap:
    def __init__(self, size=100, open_addressing=True):
        self.size = size
        self.open_addressing = open_addressing
        if open_addressing:
            self.table = [None] * size
        else:
            self.table = [[] for _ in range(size)]

    def hash(self, key):
        return hash(key) % self.size

    def find(self, key):
        idx = self.hash(key)
        if self.open_addressing:
            while self.table[idx] is not None:
                if self.table[idx][0] == key:
                    return True
                idx = (idx + 1) % self.size
            return False
        else:
            for k, v in self.table[idx]:
                if k == key:
                    return True
            return False

    def insert(self, key, value):
        idx = self.hash(key)
        if self.open_addressing:
            while self.table[idx] is not None:
                if self.table[idx][0] == key:
                    self.table[idx] = (key, value)
                    return
                idx = (idx + 1) % self.size
            self.table[idx] = (key, value)
        else:
            for i, (k, v) in enumerate(self.table[idx]):
                if k == key:
                    self.table[idx][i] = (key, value)
                    return
            self.table[idx].append((key, value))

    def remove(self, key):
        idx = self.hash(key)
        if self.open_addressing:
            while self.table[idx] is not None:
                if self.table[idx][0] == key:
                    self.table[idx] = None
                    return
                idx = (idx + 1) % self.size
        else:
            for i, (k, v) in enumerate(self.table[idx]):
                if k == key:
                    del self.table[idx][i]
                    return
