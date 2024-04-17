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

'''
The Recover Binary Search Tree problem asks us to restore a binary search tree to its original form after two of its nodes have been swapped. 
This problem requires a strong understanding of the structure and properties of a binary search tree, 
namely that all nodes to the left of the root are smaller than the root and all nodes to the right are larger.



Solution steps :
1. find the two nodes that is not in the right place (canceling the BST atribute)
    Two condition
     a. The current node is in the a middle layer of the tree or root node.
        
     b. The current node is in the last layer of the tree (leaf).
        It depend on the parent node to consodre of this is the  one of the swapped node or not.

''' 
def main():
    print("Question 11")

    
if __name__ == "__main__":
    main()          