# Leetcode problem.

import unittest


class TestInterview(unittest.TestCase):
    # Test case for interview
    def __setUp__(self):
        pass

    def test_question1(self):
        # Test scenario
        candies = [2, 3, 5, 1, 3]
        extra_candies = 3

        # Instantiation
        q = Interview()

        # Test Cases
        self.assertEqual(q.question1(candies, extra_candies), [False, True, True, False, True])


class Interview:
    def __init__(self):
        pass

    def question1(self, candies, extra_candies):
        result = []
        highest = max(candies)
        for val in candies:
            if (val + extra_candies) > highest:
                result.append(True)
            else:
                result.append(False)

        return result


if __name__ == "__main__":
    unittest.main()
