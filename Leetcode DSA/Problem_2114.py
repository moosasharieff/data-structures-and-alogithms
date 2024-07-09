

import unittest

class TestInteview(unittest.TestCase):
    def __setUp__(self):
        pass

    def test_question1(self):
        # Scenario
        li = ["alice and bob love leetcode","i think so too","this is great thanks very much"]

        # Instantiation
        q = Interview()

        # Test Cases
        self.assertEqual(q.question1(li), 6)


class Interview:
    def __init__(self):
        pass

    def question1(self, sentences):
        """
        Time Complexity: O(n) as we are iterating sentences in linear sequece and using split() method to count number of word in in one iteration.
        Space Complexity: O(1) as we are using maXCount to store the value of the max count number of words. var: val is not considered as it is a local variable.
        """
        maxCount = 0
        for sentence in sentences:
            val = sentence.split(" ")
            maxCount = max(maxCount, len(val))

        return maxCount


# Execution

if __name__ == "__main__":
    unittest.main()