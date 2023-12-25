

from unittest import TestCase
from src.Stack import Stack

class Test_Stack(TestCase):
    def setUp(self):
        self.my_stack = Stack(1)

    def test_initiation(self):
        self.assertIsNotNone(self.my_stack)
        self.assertEqual(self.my_stack.top.value, 1)


    def test_push(self):
        self.my_stack.push(2)
        self.my_stack.push(3)
        self.assertIsNotNone(self.my_stack)
        self.assertEqual(self.my_stack.top.value, 3)
        self.assertEqual(self.my_stack.top.next.value, 2)
        self.assertEqual(self.my_stack.top.next.next.value, 1)
        self.assertIsNone(self.my_stack.top.next.next.next)