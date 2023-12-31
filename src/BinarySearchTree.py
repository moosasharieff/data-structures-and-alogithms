

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
