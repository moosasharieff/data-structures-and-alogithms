
from unittest import TestCase
from src.DoublyLinkedList import DoublyLinkedList

class Test_Doubly_LinkedList(TestCase):

    def setUp(self):
        self.dll = DoublyLinkedList(1)

    def test_append(self):

        # handling no nodes
        self.assertIsNotNone(self.dll.tail.val)
        # handling single nodes
        self.dll.append(2)
        self.assertIsNotNone(self.dll.tail.head.val)
        self.assertEqual(self.dll.tail.head.val, 2)
        # handling mulitple nodes
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.assertIsNotNone(self.dll.tail.head.val)
        self.assertEqual(self.dll.head.val, 1)
        self.assertEqual(self.dll.head.next.head.val, 2)
        self.assertEqual(self.dll.tail.head.val, 3)

    def test_pop(self):
        # handling single nodes
        self.dll.pop()
        self.assertIsNone(self.dll.head)
        # handling no nodes
        self.dll.pop()
        self.assertIsNone(self.dll.head)
        # handling multiple nodes
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.assertEqual(self.dll.head.head.val, 1)
        self.assertEqual(self.dll.head.next.head.val, 2)
        self.assertEqual(self.dll.tail.head.val, 3)
        self.dll.pop()
        self.assertIsNotNone(self.dll)
        self.assertEqual(self.dll.head.head.val, 1)
        self.assertIsNotNone(self.dll.tail)
        self.assertEqual(self.dll.tail.head.val, 2)