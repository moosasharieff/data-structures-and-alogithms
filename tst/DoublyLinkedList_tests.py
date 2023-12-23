
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
        self.assertIsNotNone(self.dll.tail.val)
        self.assertEqual(self.dll.tail.val, 2)
        # handling mulitple nodes
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.assertIsNotNone(self.dll.tail.val)
        self.assertEqual(self.dll.head.val, 1)
        self.assertEqual(self.dll.head.next.val, 2)
        self.assertEqual(self.dll.tail.val, 3)

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

    def test_prepend(self):
        # Making sure it has no nodes
        self.dll.pop()
        self.assertIsNone(self.dll.head)
        # When no node
        self.dll.prepend(2)
        self.assertEqual(self.dll.head.val, 2)
        self.assertEqual(self.dll.tail.val, 2)
        # When 1 or more nodes
        self.assertIsNotNone(self.dll.head)
        self.dll.prepend(1)
        self.assertEqual(self.dll.head.val, 1)
        self.assertEqual(self.dll.tail.val, 2)

    def test_pop_first(self):
        # When there is 1 node
        self.assertEqual(self.dll.head.val, 1)
        self.dll.pop_first()
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)

        # When no node
        self.assertIsNone(self.dll.pop_first())

        # When 1+ more nodes
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.assertIsNotNone(self.dll)
        self.assertEqual(self.dll.head.val, 1)
        self.assertAlmostEqual(self.dll.head.next.val, 2)
        self.assertEqual(self.dll.tail.val, 3)

    def test_get(self):
        # Out of range index
        self.assertIsNone(self.dll.get(2))
        self.assertIsNone(self.dll.get(1))

        # When there is only 1 Node
        self.assertEqual(self.dll.get(0).val, 1)

        # When there are 1+ Nodes
        self.dll.append(2)
        self.dll.append(3)
        self.dll.append(4)
        # close index
        self.assertEqual(self.dll.get(1).val, 2)
        # Far index
        self.assertEqual(self.dll.get(2).val, 3)

    def test_set_value(self):
        """
        # Testing out of range
        # Testing 1st index value
        # Testing last index value
        # Testing middle index value
        """
        # Testing out of range
        self.assertIsNone(self.dll.get(2))
        self.assertIsNone(self.dll.get(1))

        # Testing 1st index value
        self.assertFalse(self.dll.set_value(1, 4))
        self.assertTrue(self.dll.set_value(0, 5))
        self.assertEqual(self.dll.head.val, 5)

        # Testing last index value
        self.dll.append(4)
        self.dll.append(3)
        self.dll.append(2)
        self.dll.append(1)
        self.assertTrue(self.dll.set_value(4, 9))
        self.assertEqual(self.dll.get(4), 9)

        # Testing middle index value
        self.assertTrue(self.dll.set_value(2, 7))
        self.assertEqual(self.dll.get(2), 7)

    def test_insert(self):
        """
        # Conditions to consider when Testing:
        1. Out of range
        2. Append
        3. Prepend
        4. Adding node in the middle
        """
        # Cleaning LinkedList
        self.dll.pop()
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)

        # 1. Out of range
        self.assertFalse(self.dll.insert(-1, 2))
        self.assertFalse(self.dll.insert(1, 3))

        # 2. Append
        self.assertTrue(self.dll.insert(0, 5))
        self.assertTrue(self.dll.insert(0, 4))
        self.assertEqual(self.dll.get(0).val, 4)
        self.assertEqual(self.dll.get(1).val, 5)

        # 3. Prepend
        self.assertTrue(self.dll.insert(2, 6))
        self.assertEqual(self.dll.get(2).val, 6)

        # 4. Adding node in the middle
        self.dll.insert(2, 9)
        self.assertEqual(self.dll.get(2).val, 9)