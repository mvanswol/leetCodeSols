#
#
# Created By : Mitchell Van Swol
# Date : 5/9/2018
#

import sys

# find the smallest positive missing number
class Solution(object):
	def firstMissingPositive(self, nums):

		if not nums:
			return 1

		size = len(nums)

		i = 0
		while i < size:
			if nums[i] < 1 or nums[i] > size: 
				i += 1
			else:
				if nums[nums[i] - 1] == nums[i]:
					i += 1
					continue
				temp = nums[nums[i] - 1]
				nums[nums[i] - 1] = nums[i]
				nums[i] = temp


		for i in range(size):
			if nums[i] != i + 1:
				return i + 1

		return size + 1
