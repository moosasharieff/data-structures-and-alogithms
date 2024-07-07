#

import unittest


class TestInterview(unittest.TestCase):
    def __setUp__(self):
        pass

    def test_question1(self):
        # Scenario
        nums = [10, 4, 8, 3]

        # Instantiation
        q = Interview()

        # Test cases
        self.assertEqual(q.question1(nums), [15, 1, 11, 22])


class Interview:
    def __init__(self):
        pass

    def question1(self, nums):
        n = len(nums)
        left = 0
        right = sum(nums)
        result = []

        for i in range(n):
            right -= nums[i]
            result.append(abs(left - right))
            left += nums[i]

        return result


if __name__ == "__main__":
    unittest.main()