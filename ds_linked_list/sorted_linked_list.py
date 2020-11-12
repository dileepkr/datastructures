from ds_linked_list.ll_node import Node

class Unsorted_linked_list:
    def __init__(self):
        self.head = None
    
    def add(self, element):
        node_ = Node(element)
        if not self.head:
            self.head = node_
        else:
            node_.next = self.head.next
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
        node_ = Node(element)
        current = self.head
        previous = None

        while current is not None and node_.data != current.data:
            previous = current
            current = current.next
            
        if previous:
            previous.next = current.next
        elif current:
            self.head = current.next
        else:
            raise ValueError("No matching element found in list to remove")

    def index(self, element):
        count = 0
        node_ = Node(element)
        current = self.head

        while current is not None and node_.data != current.data:
            count += 1
            current = current.next
        
        return count

    def pop(self):
        if not self.head:
            return None

        if not self.head.next:
            data = self.head.data
            self.head = None
            return data

        previous = None
        current = self.head
        while current is not None and current.next is not None:
            previous = current
            current = current.next
        previous.next = current.next
        return current.data

    def pop(self, position):
        if not self.head:
            return self.head
        
        count = 0
        previous = None
        current = self.head
        while count != position and current.next is not None:
            count += 1
            previous = current
            current = current.next
        
        if count != position:
            raise IndexError("Provided list index out of bound")
        if not previous:
            self.head = current.next
        else:
            previous.next = current.next
        return current.data

    def search(self, element):
        if not self.head:
            raise ValueError("Empty List, value not found")

        node_ = Node(element)
        current = self.head
        while current is not None and node_.data != current.data:
            current = current.next
        if not current:
            return False
        return True

    def __repr__(self) -> str:
        ret_list = []
        current = self.head
        while current is not None:
            ret_list.append(current.data)
            current = current.next
        return ret_list

if __name__ == "__main__":
    ll = Unsorted_linked_list()
    for i in range(1,10):
        ll.add(i)
    print(ll)