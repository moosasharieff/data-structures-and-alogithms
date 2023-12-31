

class Node:
    def __init__(self, value):
        """ Creates a node for BST """
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        """
        Constructor for Binary Search Tree.
        Initilizes empty tree. Nodes can be added from insert method.
        """
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        # check if root is empty
        if self.root is None:
            self.root = new_node
            return True

        # Traverse through the tree
        temp = self.root
        while True:
            # check if new_node's value is already present
            if new_node.value == temp.value:
                return False

            # Moving inside the tree
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

