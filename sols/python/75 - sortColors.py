

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        start = 0
        i = 0
        end = len(nums) - 1

        while i  <= end:

            if nums[i] == 0:
                nums[i], nums[start] = nums[start], nums[i]
                start += 1
            elif nums[i] == 2:
                nums[i], nums[end] = nums[end], nums[i]
                end -= 1
                i -= 1
            i += 1