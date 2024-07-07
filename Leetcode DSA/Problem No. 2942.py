

import unittest

class TestInterview(unittest.TestCase):
    def __setUp__(self):
        pass

    def test_question1(self):
        # Args
        li = ["leet", "code"]
        x = 'e'

        # Instantiating
        q = Interview()

        # Testcases
        self.assertEqual(q.question1(li, x), [0, 1])


class Interview:
    def __init__(self):
        pass

    def question1(self, li, x):
        counter = []
        for idx, val in enumerate(li):
            if x in val:
                counter.append(idx)

        return counter


if __name__ == "__main__":
    unittest.main()