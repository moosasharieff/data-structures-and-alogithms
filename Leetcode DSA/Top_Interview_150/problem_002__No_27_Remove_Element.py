

class Remove_Element:
    def __init__(self):
        pass

    def question1(self, nums, val):
        """Removing elements in one place"""
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k

