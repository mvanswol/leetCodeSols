#
#
# Created By : Mitchell Van Swol
# Date : 6/18/2018
#

import sys

# solve the maximum sub array problem
class Solution(object):
	def maxSubArray(self, nums):

		if len(nums) < 1:
			return 0

		total = maxSub = nums[0]

		for i in range(1, len(nums)):
			total = max(total+nums[i], nums[i])
			maxSub = max(total, maxSub)

		return maxSub