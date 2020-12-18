from ds_trees.bst import BinarySearchTree, TreeNode

class AVLTree(BinarySearchTree):
    def __init__(self) -> None:
        super().__init__()
    
    def _put(self, key, val, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, val, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key=key, val=val, parent=current_node)
                self.update_balance(current_node.left_child)
        else:
            if current_node.has_right_child():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key=key, val=val, parent=current_node)
                self.update_balance(current_node.right_child)

    def update_balance(self, node):
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)
            return
        if node.parent != None:
            if node.is_left_child():
                node.parent.balance_factor += 1
            elif node.is_right_child():
                node.parent.balance_factor -= 1
            
            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)
    
    def rebalance(self, node):
        if node.balance_factor < 0:
            #it means it is right heavy
            #conduct a left rotation
            if node.right_child.balance_factor > 0:
                self.rotate_right(node.right_child)
                self.rotate_left(node)
            else:
                self.rotate_left(node)
        elif node.balance_factor > 0:
            #it means the tree is left heavy
            #rotate the node to the right
            if node.left_child.balance_factor < 0:
                self.rotate_left(node.left_child)
                self.rotate_right(node)
            else:
                self.rotate_right(node)

    def rotate_left(self, rot_root):
        #save root to be shifted in temp variable
        new_root = rot_root.right_child
        #shift the left_child of new root to the right child of current root
        rot_root.right_child = new_root.left_child
        if new_root.left_child:
            new_root.left_child.parent = rot_root
        #link parent of current root to new root
        new_root.parent = rot_root.parent
        #link current root's parent's child references to new root
        if rot_root.is_root():
            self.root = new_root
        else:
            if rot_root.is_left_child():
                rot_root.parent.left_child = new_root
            elif rot_root.is_right_child():
                rot_root.parent.right_child = new_root
        #make new root as current root's parent
        rot_root.parent = new_root
        new_root.left_child = rot_root

        #update balance factors
        rot_root.balance_factor = rot_root.balance_factor + 1 - min(0, new_root.balance_factor)
        new_root.balance_factor = new_root.balance_factor + 1 + max(0, rot_root.balance_factor)

    def rotate_right(self, rot_root):
        new_root = rot_root.left_child
        rot_root.left_child = new_root.right_child
        if new_root.right_child:
            new_root.right_child.parent = rot_root
        
        new_root.parent = rot_root.parent
        if rot_root.is_root():
            self.root = new_root
        else:
            if rot_root.is_right_child():
                rot_root.parent.right_child = new_root
            elif rot_root.is_left_child():
                rot_root.parent.left_child = new_root
            
        rot_root.parent = new_root
        new_root.right_child = rot_root

        rot_root.balance_factor = rot_root.balance_factor + 1 - min(0, new_root.balance_factor)
        new_root.balance_factor = new_root.balance_factor + 1 + max(0, rot_root.balance_factor)

