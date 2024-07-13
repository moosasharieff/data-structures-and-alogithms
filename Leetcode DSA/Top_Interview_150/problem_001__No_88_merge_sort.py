

class Merge_Sort:
    def __init__(self):
        pass

    def merge_sort(self, nums1, nums2, m, n):
        last = (m + n)

        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n -1]:
                nums1[last - 1] = nums1[m -1]
                m -= 1
            else:
                nums1[last - 1] = nums2[n - 1]
                n -= 1

            last -= 1

        # Handling the edge case
        while n > 0:
            nums1[last - 1] = nums2[n - 1]
            last -= 1
            n -= 1


