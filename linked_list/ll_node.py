class Node:
    def  __init__(self, initdata) -> None:
        self.data = initdata
        self.next = None
    
    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext