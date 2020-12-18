class BinarySearchTree:
    """
    Property: Keys less than parent are found in the left tree, 
    Keys greater than parent are found in the right tree.
    each subtree is a BST
    """
    def __init__(self) -> None:
        self.root = None
        self.size = 0
    
    def length(self):
        return self.size
    
    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1
    
    def _put(self, key, val, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, val, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, val, parent=current_node)
        else:
            if current_node.has_right_child():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, val, parent=current_node)
    
    def __setitem__(self, key, val):
        self.put(key, val)
    
    def get(self, key):
        if self.root:
            result = self._get(key, self.root)
            if result:
                return result.payload
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)
    
    def __getitem__(self, key):
        return self.get(key=key)

    def __contains__(self, key):
        if self.get(key):
            return True
        else:
            return False
    
    def delete(self, key):
        if self.size > 1:
            node_to_delete = self.get(key)
            if node_to_delete:
                self.remove(node_to_delete)
                self.size -= 1
            else:
                raise KeyError(f"Given key {key} not found in binary search tree.")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError(f"Given key {key} not found in binary search tree.")

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, node_to_remove):
        if node_to_remove.is_leaf():
            if node_to_remove.is_left_child():
                node_to_remove.parent.left_child = None
            else:
                node_to_remove.parent.right_child = None
        elif node_to_remove.has_both_children():
            succ = node_to_remove.find_successor()
            # Successor will be a node with 1 or zero children
            succ.splice_out()
            node_to_remove.key = succ.key
            node_to_remove.payload = succ.payload
        else:
            if node_to_remove.has_left_child():
                if node_to_remove.is_left_child():
                    node_to_remove.left_child.parent = node_to_remove.parent
                    node_to_remove.parent.left_child = node_to_remove.left_child
                elif node_to_remove.is_right_child():
                    node_to_remove.left_child.parent = node_to_remove.parent
                    node_to_remove.parent.right_child = node_to_remove.right_child
                else:
                    node_to_remove.replace_node_data(
                        node_to_remove.left_child.key,
                        node_to_remove.left_child.payload,
                        node_to_remove.left_child.left_child,
                        node_to_remove.left_child.right_child,
                    )
            else:
                if node_to_remove.is_left_child():
                    node_to_remove.right_child.parent = node_to_remove.parent
                    node_to_remove.parent.left_child = node_to_remove.right_child
                elif node_to_remove.is_right_child():
                    node_to_remove.right_child.parent = node_to_remove.parent
                    node_to_remove.parent.right_child = node_to_remove.right_child
                else:
                    node_to_remove.replace_node_data(
                        node_to_remove.right_child.key,
                        node_to_remove.right_child.payload,
                        node_to_remove.right_child.left_child,
                        node_to_remove.right_child.right_child,
                    )
        self.size -= 1

    
    def __str__(self) -> str:
        if self:
            for node in self.root:
                print(node)



class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None, balance_factor=None) -> None:
        self.key = key
        self.payload = val
        self.left_child = left
        self.right_child = right
        self.parent = parent
        self.balance_factor = balance_factor
    
    def has_left_child(self):
        return self.left_child
    
    def has_right_child(self):
        return self.right_child
    
    def is_left_child(self):
        return (self.parent and self.parent.left_child == self)
    
    def is_right_child(self):
        return (self.parent and self.parent.right_child == self)
    
    def is_root(self):
        return not self.parent
    
    def is_leaf(self):
        return (not self.left_child and not self.right_child)
    
    def has_any_children(self):
        return self.left_child or self.right_child
    
    def has_both_children(self):
        return self.left_child and self.right_child
    
    def replace_node_data(self, key, val, lc, rc):
        self.key = key
        self.val = val
        self.left_child = lc
        self.right_child = rc
        if self.has_left_child:
            self.left_child.parent = self
        if self.has_right_child:
            self.right_child.parent = self

    def find_successor(self):
        successor = None
        if self.has_right_child():
            successor = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    successor = self.parent
                else:
                    self.parent.right_child = None
                    successor = self.parent.find_successor()
                    self.parent.right_child = self
        return successor
    
    def find_min(self):
        current = self
        while current.has_left_child():
            current = current.left_child
        return current
    
    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        else:
            if self.has_any_children():
                if self.has_left_child():
                    if self.is_left_child():
                        self.parent.left_child = self.left_child
                    else:
                        self.parent.right_child = self.left_child
                    self.left_child.parent = self.parent
                else:
                    if self.is_left_child():
                        self.parent.left_child = self.right_child
                    else:
                        self.parent.right_child = self.right_child
                    self.right_child.parent = self.parent

    def __iter__(self):
        if self:
            if self.has_left_child():
                for elem in self.left_child:
                    yield elem
            yield self.key
            if self.has_right_child():
                for elem in self.right_child:
                    yield elem



if __name__ == "__main__":
    mytree = BinarySearchTree()
    mytree[3]="red"
    mytree[4]="blue"
    mytree[6]="yellow"
    mytree[2]="black"

    print(mytree)