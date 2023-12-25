

from unittest import TestCase
from src.Queue import Queue

class Test_Queue(TestCase):
    def setUp(self):
        """ Setups the requirements for running test cases """
        self.myQueue = Queue(1)

    def test_constructor(self):
        self.assertIsNotNone(self.myQueue)
        self.assertEqual(self.myQueue.first.value, 1)

    def test_enqueue(self):
        self.assertEqual(self.myQueue.first.value, 1)
        self.assertEqual(self.myQueue.last.value, 1)
        # Adding value to the queue
        self.myQueue.enqueue(2)
        self.assertEqual(self.myQueue.last.value, 2)


    def test_dequeue(self):
        """ Remove the value from the queue
        Things to consider :
        1. Testing when Queue is empty
        2. Testing when Queue has only 1 node
        3. Testing when Queue has 1+ nodes
        """
        self.myQueue.enqueue(2)
        self.myQueue.enqueue(3)
        self.assertEqual(self.myQueue.first.value, 1)
        self.assertEqual(self.myQueue.last.value, 3)

        # Testing dequeue() method
        # 3. Testing when Queue has 1+ nodes
        self.assertEqual(self.myQueue.dequeue().value, 1)
        self.assertEqual(self.myQueue.dequeue().value, 2)
        # 2. Testing when Queue has only 1 node
        self.assertEqual(self.myQueue.dequeue().value, 3)
        # 1. Testing when Queue is empty
        self.assertIsNone(self.myQueue.dequeue())