class CustomStack:
    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize
        self.increment_values = [0] * maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        index = len(self.stack) - 1
        if index > 0:
            self.increment_values[index - 1] += self.increment_values[index]
        result = self.stack.pop() + self.increment_values[index]
        self.increment_values[index] = 0
        return result

    def increment(self, k: int, val: int) -> None:
        if self.stack:
            limit = min(k, len(self.stack)) - 1
            self.increment_values[limit] += val


