class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = []
        self.stack = []
        self.count = 0
        self.k = k

    def enQueue(self, x: int) -> bool:
        if self.count < self.k:
            self.count += 1
            while self.queue:
                self.stack.append(self.queue.pop())
            self.queue.append(x)
            for i in range(self.count - 1):
                self.queue.append(self.stack.pop())
            self.stack.append(x)
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.count > 0:
            self.count -= 1
            self.queue.pop()
            return True
        else:
            return False

    def Front(self) -> int:
        if self.count > 0:
            return self.queue[-1]
        else:
            return -1

    def Rear(self) -> int:
        if self.count > 0:
            return self.stack[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k
