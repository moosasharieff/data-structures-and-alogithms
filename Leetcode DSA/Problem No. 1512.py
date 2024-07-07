

import unittest


class InterviewQuestion:
    def question1(self, li):
        # Writing the logic
        count = 0
        for i in range(len(li) - 1):
            for j in range(i + 1, len(li)):
                if li[i] == li[j] and i < j:
                    count += 1

        return count


class InterviewTest(unittest.TestCase):
    """Test cases for question asked in the interview"""

    def test_question1(self):
        li = [1, 2, 3, 1, 1, 3]

        # Instantiating
        q = InterviewQuestion()

        # Test cases
        self.assertEqual(q.question1(li), 4)


if __name__ == "__main__":
    unittest.main()