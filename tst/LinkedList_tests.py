

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

    def test_prepend(self):

        """
        1. If there is no Node in the LL
        2. If there is 1 or more nodes in the LL
        :return:
        """
        # 1. If there is no Node in the LL
        # checking if None
        self.ll.pop()

        # checking if value has been added, returns True
        self.assertTrue(self.ll.prepend(2))

        # checking its value
        self.assertEqual(self.ll.head.value, 2)

        # 2. If there is 1 or more nodes in the LL
        self.ll.append(3)
        self.ll.append(4)
        # Checking the length
        self.assertEqual(self.ll.length, 3)

    def test_pop_first(self):
        """
        1. if there is no node in LL
        2. if there is only 1 node in LL
        3. if there is 1+ nodes in LL
        :return:
        """
        # 2. if there is only 1 node in LL
        self.ll.pop()
        self.assertIsNone(self.ll.head)

        # 3. if there is 1+ nodes in LL
        self.ll.append(1)
        self.ll.append(2)
        # checking value and length
        self.assertEqual(self.ll.length, 2)
        self.assertEqual(self.ll.head.value, 1)
        self.assertEqual(self.ll.tail.value, 2)

    def test_get(self):
        self.ll.append(2)
        self.ll.append(3)
        self.ll.append(4)

        self.assertEqual(self.ll.get(1).value,2)
        self.assertEqual(self.ll.get(3).value, 4)
        self.assertEqual(self.ll.length, 4)

    def test_insert(self):
        """
            # Test Case:
            1. If index is 0 or greater than LL Length
            2. Use prepend to add in beginning
            3. Use append to add in the end
            4. Need logic to add in between
        """
        # 1. If index is 0 or greater than LL Length
        self.assertFalse(self.ll.insert(-1, 3))

        # 2. Use prepend to add in beginning
        self.ll.insert(0,9)
        self.assertEqual(self.ll.head.value, 9)

        # 3. Use append to add in the end
        print(self.ll.length)
        self.ll.insert(self.ll.length, 7)
        self.assertEqual(self.ll.tail.value, 7)


    def test_set_value(self):
        # Editing value at 0 Index
        self.ll.set_value(0, 4)
        self.assertEqual(self.ll.head.value, 4)

        # Editing value at in middle
        new_ll = LinkedList(1)
        new_ll.append(2)
        new_ll.append(3)
        new_ll.set_value(2, 5)
        self.assertEqual(new_ll.get(2).value, 5)

    def test_remove(self):
        """
            Test cases:
            0. If index provided is out of range
            1. If there is no node in LL
            2. If we are to remove 1st node in LL
            3. If we are remove last node in LL
            4. If we are to remove middle node in the LL
        """
        # 0. If index provided is out of range
        self.assertIsNone(self.ll.remove(-1))
        self.assertIsNone(self.ll.remove(2))

        # 2. If we are to remove 1st node in LL
        self.assertEqual(self.ll.remove(0).value, 1)
        # 1. If there is no node in LL
        self.assertIsNone(self.ll.remove(0))
        self.assertIsNone(self.ll.remove(1))
        # 3. If we are remove last node in LL
        self.ll.append(7)
        self.ll.append(8)
        self.ll.append(9)
        self.assertEqual(self.ll.remove(1).value, 8)
        self.assertEqual(self.ll.remove(2).value, 9)
