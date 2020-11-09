class Queue:
    def __init__(self) -> None:
        self._container = []

    def enqueue(self, element) -> None:
        self._container.insert(0, element)

    def dequeue(self):
        return self._container.pop()

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self._container)