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
                self._put(key, val, current_node.leftchild)
            else:
                current_node.leftchild = TreeNode(key, val, parent=current_node)
        else:
            if current_node.has_right_child():
                self._put(key, val, current_node.rightchild)
            else:
                current_node.rightchild = TreeNode(key, val, parent=current_node)
    
    def __setiterm__(self, key, val):
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
            return self._get(key, current_node.leftchild)
        else:
            return self._get(key, current_node.rightchild)
    
    def __getitem__(self, key):
        return self.get(key=key)

    def __contains__(self, key):
        if self.get(key):
            return True
        else:
            return False
    
    def delete(self, key):
        pass

class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None) -> None:
        self.key = key
        self.payload = val
        self.leftchild = left
        self.rightchild = right
        self.parent = parent
    
    def has_left_child(self):
        return self.leftchild
    
    def has_right_child(self):
        return self.rightchild
    
    def is_left_child(self):
        return (self.parent and self.parent.leftchild == self)
    
    def is_right_child(self):
        return (self.parent and self.parent.rightchild == self)
    
    def is_root(self):
        return not self.parent
    
    def is_leaf(self):
        return (not self.leftchild and not self.rightchild)
    
    def has_any_children(self):
        return self.leftchild or self.rightchild
    
    def has_both_children(self):
        return self.leftchild and self.rightchild
    
    def replace_node_data(self, key, val, lc, rc):
        self.key = key
        self.val = val
        self.leftchild = lc
        self.rightchild = rc
        if self.has_left_child:
            self.leftchild.parent = self
        if self.has_right_child:
            self.rightchild.parent = self


