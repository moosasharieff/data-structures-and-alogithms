

from unittest import TestCase
from src.Stack import Stack

class Test_Stack(TestCase):
    def setUp(self):
        self.my_stack = Stack(1)

    def test_initiation(self):
        self.assertIsNotNone(self.my_stack)
        self.assertEqual(self.my_stack.top.value, 1)