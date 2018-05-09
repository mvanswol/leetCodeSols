#
#
# Created By : Mitchell Van Swol
# Date : 5/8/2018
#

import sys

# Search rotated Sorted numsay


class Solution(object):
	def search(self, nums, target):

		if not nums:
			return -1

		low, high = 0, len(nums) - 1

		while low <= high:
			mid = (low + high)/2

			if target == nums[mid]:
				return mid

			if nums[low] <= nums[mid]:
				if nums[low] <= target <= nums[mid]:
					high = mid - 1
				else:
					low = mid + 1
			else:
				if nums[mid] <= target <= nums[high]:
					low = mid + 1
				else:
					high = mid - 1

		return -1


