

from unittest import TestCase
from src.Queue import Queue

class Test_Queue(TestCase):
    def setUp(self):
        """ Setups the requirements for running test cases """
        self.myQueue = Queue(1)

    def test_constructor(self):
        self.assertIsNotNone(self.myQueue)
        self.assertEqual(self.myQueue.first.value, 1)

