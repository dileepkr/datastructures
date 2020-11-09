from typing import Deque


class Deque:
    def __init__(self) -> None:
        self._container = []
    
    def addFront(self, element):
        self._container.append(element)
    
    def addRear(self, element):
        self._container.insert(0, element)
    
    def removeFront(self):
        return self._container.pop()
    
    def removeRear(self):
        return self._container.pop(0)
    
    def isEmpty(self):
        return self._container == []
    
    def size(self):
        return len(self._container)