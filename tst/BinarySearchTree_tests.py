

from unittest import TestCase
from src.BinarySearchTree import BinarySearchTree, Node

class Test_BinarySearchTree(TestCase):

    def setUp(self):
        self.tree = BinarySearchTree()

    def test_node(self):
        new_node = Node(1)
        self.assertIsNotNone(new_node)

    def test_constructor(self):
        self.assertIsNone(self.tree.root)

