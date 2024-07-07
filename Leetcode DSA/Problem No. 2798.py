# Time Complexity: O(nlogn) as we are using sort() here.
# Space Complexity: O(1) as we are add results only in a single variable

import unittest


class TestInterview(unittest.TestCase):
    # Test cases for interview
    def setUp(self):
        pass

    def test_question1(self):
        # Test scenario
        hours = [0, 1, 2, 3, 4]
        target = 2

        # Instantiation
        q = Interview()

        # Test case
        self.assertEqual(q.question1(hours, target), 3)
        self.assertEqual(q.question1([5, 1, 4, 2, 2], 6), 0)


class Interview:
    def __init__(self):
        pass

    def question1(self, hours, target):
        hours.sort(reverse=True)

        count = 0
        for val in hours:
            if val >= target:
                count += 1
            else:
                break

        return count


if __name__ == "__main__":
    unittest.main()