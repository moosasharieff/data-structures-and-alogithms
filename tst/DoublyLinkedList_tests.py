
from unittest import TestCase
from src.DoublyLinkedList import DoublyLinkedList

class Test_Doubly_LinkedList(TestCase):

    def setUp(self):
        self.dll = DoublyLinkedList(1)

    def test_append(self):
        # checks the first value of the Doubly LinkedList
        self.assertEqual(self.dll.head.val, 1)
        self.dll.append(2)
        # checks the last value of the Doubly LinkedList
        self.assertEqual(self.dll.tail.head.val, 2)