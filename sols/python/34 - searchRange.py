#
#
# Created By : Mitchell Van Swol
# Date : 5/8/2018
#

import sys

# Search for a range

class Solution(object):
	def searchRange(self, nums, target):

		if not nums:
			return [-1,-1]


		low, high = 0, len(nums) - 1
		first, last = -1, -1

		while low <= high:
			mid = int((low + high)/2)

			if nums[mid] == target:
				if first == -1: # we haven't found the start yet
					if mid-1 == -1 or nums[mid-1] < target: # check to see if there is
					                                     # the same value further to the left
						first = mid
						low, high = 0, len(nums) - 1
					else:
						high = mid - 1
				else:
					if mid+1 == len(nums) or nums[mid + 1] > target: # check right for vals
						last = mid
						break
					else:
						low = mid + 1

			elif nums[mid] > target:
				high = mid - 1
			else:
				low = mid + 1

		return [first, last]