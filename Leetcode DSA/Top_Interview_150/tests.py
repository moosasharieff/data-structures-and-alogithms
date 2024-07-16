
import unittest
from problem_001__No_88_merge_sort import Merge_Sort
from problem_002__No_27_Remove_Element import Remove_Element

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

    def test_remove_element(self):
        # Scenario
        nums1 = [0 ,1 ,2 ,2 ,3 ,0 ,4 ,2]
        val1 = 2

        nums2 = [3, 2, 2, 3]
        val2 = 2

        # Instantiation
        q = Remove_Element()

        # Test Cases
        self.assertEqual(q.question1(nums1, val1), 5)
        self.assertEqual(q.question1(nums2, val2), 2)




if __name__ == "__main__":
    unittest.main()