

from unittest import TestCase
from src.LinkedList import LinkedList

class Test_LinkedList(TestCase):

    def setUp(self):
        self.ll = LinkedList(1)

    def test_LinkedList_Object(self):

        self.assertIsInstance(self.ll, LinkedList)
        self.assertAlmostEqual(self.ll.length, 1)

    def test_append(self):
        self.ll.append(2)
        self.assertIsNotNone(self.ll)
        self.assertEqual(self.ll.length, 2)
        self.assertEqual(self.ll.tail.value, 2)
        self.assertIsNone(self.ll.tail.next)

    def test_pop(self):
        # Appending more values to the LL
        self.ll.append(2)
        self.ll.append(3)

        self.ll.pop()
        self.assertEqual(self.ll.length, 2)
        self.ll.pop()
        self.assertEqual(self.ll.length, 1)
        self.ll.pop()
        self.assertIsNone(self.ll.pop())  # There is no node in LL