#
#
# Created By : Mitchell Van Swol
# Date : 5/8/2018
#

import sys

# Search for insert spot

class Solution(object):
    def searchInsert(self, nums, target):

        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = int((low + high)/2)

            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return low