from ds_linked_list.ll_node import Node

class Unsorted_linked_list:
    def __init__(self):
        self.head = None
    
    def add(self, element):
        node_ = Node(element)
        self.head = node_

    def length(self):
        current = self.head
        count = 0
        while current != None or current.next != None:
            count += 1
            current = current.next
        return count
    
    def is_empty(self):
        return self.head == None

    def remove(self, element):
        pass

    def index(self, element):
        pass

    def pop(self):
        pass

    def pop(self, position):
        pass

    def search(self, element):
        pass