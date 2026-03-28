class MyQueue:

    def __init__(self):
        self.queue = []
        self.stack = []
        self.count = 0

    def push(self, x: int) -> None:
        self.count += 1
        while self.queue:
            self.stack.append(self.queue.pop())
        self.queue.append(x)
        for i in range(self.count - 1):
            self.queue.append(self.stack.pop())

    def pop(self) -> int:
        self.count -= 1
        return self.queue.pop()

    def peek(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return not self.queue
