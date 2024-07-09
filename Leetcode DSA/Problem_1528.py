import unittest


class Interview:
    def __init__(self):
        pass

    def question1(self, s, indices):
        ans = [0 for i in range(len(s))]

        for i in range(len(s)):
            ans[indices[i]] = s[i]

        val = "".join(ans)

        return val


class TestInterview(unittest.TestCase):
    def __setUp__(self):
        pass

    def test_question1(self):
        # Scenario
        s = "codeleet"
        indices = [4, 5, 6, 7, 0, 2, 1, 3]

        # Instantiation
        q = Interview()

        # Test case
        self.assertEqual(q.question1(s, indices), "leetcode")

# Execution
if __name__ == "__main__":
    unittest.main()