class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while (temp is not None):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def recursive_insert(self, value, temp):
        if self.root is None:
            self.root = Node(value)
            return True
        if value == temp.value:
            return False
        if value < temp.value:
            if temp.left is None:
                temp.left = Node(value)
                return True
            self.recursive_insert(value,temp.left)
        else:
            if temp.right is None :
                temp.right = Node(value)
                return True
            self.recursive_insert(value,temp.right)

    def print_tree(self,temp: Node):
        if temp is not None:
            if temp.left is not None:
                self.print_tree(temp.left)
            if temp.right is not None:
                self.print_tree(temp.right)
            print(temp.value)

        
        

        
tree = BinarySearchTree()

tree.recursive_insert(10,tree.root)
tree.recursive_insert(15,tree.root)
tree.recursive_insert(8,tree.root)
tree.recursive_insert(9,tree.root)



# print(tree.root.value)
# print(tree.root.right.value)
# print(tree.root.left.value)


tree.print_tree(tree.root)
# my_tree = BinarySearchTree()
# my_tree.insert(47)
# my_tree.insert(21)
# my_tree.insert(76)
# my_tree.insert(18)
# my_tree.insert(27)
# my_tree.insert(52)
# my_tree.insert(82)

# print('BST Contains 27:')
# print(my_tree.contains(27))

# print('\nBST Contains 17:')
# print(my_tree.contains(17))
                


"""
    EXPECTED OUTPUT:
    ----------------
    BST Contains 27:
    True

    BST Contains 17:
    False

"""