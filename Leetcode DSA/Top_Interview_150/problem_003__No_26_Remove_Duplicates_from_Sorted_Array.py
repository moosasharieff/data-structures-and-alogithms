

class Remove_Duplicate:
    def __init__(self):
        pass

    def logic(self, nums):
        """Remove duplicates and returns k - length of unique elements.
        :return int """
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k