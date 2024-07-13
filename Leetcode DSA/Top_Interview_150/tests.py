
import unittest
from problem_001__No_88_merge_sort import Merge_Sort

class TestLeetcodeProblems(unittest.TestCase):

    def __setUp__(self):
        pass

    def test_merge_sort(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        nums2 = [2, 5, 6]
        m = 3
        n = 3

        # Instantiation
        q = Merge_Sort()
        q.merge_sort(nums1, nums2, m, n)

        # Test cases
        self.assertEqual(nums1, [1,2,2,3,5,6])



if __name__ == "__main__":
    unittest.main()