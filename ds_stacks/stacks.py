class Stack:
    '''
    Abstact Stack datatype implementation in python
    This version uses a python list to implement stack,
    base of stack is first element of the list, 
    top of stack is end of the list.
    '''
    def __init__(self) -> None:
        self._container = []
    
    def push(self, item):
        self._container.append(item)
    
    def pop(self):
        self._container.pop()
    
    def peak(self):
        return self._container[self.size() - 1]
    
    def is_empty(self):
        return self._container == []
    
    def size(self):
        return len(self._container)
    
    def to_list(self):
        return self._container[::-1]
    
    def __str__(self) -> str:
        return ''.join([str(elem) for elem in self.to_list()])