
import unittest

class TestInterview(unittest.TestCase):

    def __setUp__(self):
        pass

    def test_question1(self):
        # Base
        li = [5 ,4 ,3 ,2]

        # Instantiation
        q = Interview()

        # Test Cases
        self.assertEqual(q.question1(li), [3 ,2 ,5 ,4])


class Interview:

    def __init__(self):
        pass

    def question1(self, ans):
        n = len(ans) // 2
        arr = []
        for _ in range(n):

            # Removing values
            a = min(ans)
            ans.remove(a)

            b = min(ans)
            ans.remove(b)

            # Appending values
            arr.append(b)
            arr.append(a)

        return arr


# Execution
if __name__ == "__main__":
    unittest.main()