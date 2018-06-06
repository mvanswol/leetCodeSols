#
#
# Created By : Mitchell Van Swol
# Date : 6/5/2018
#

import sys

# jump game problem
class Solution(object):
	def jump(self, nums):

		best_reachable = 0
		new_best_reachable = 0
		i = 0
		count = 0
		length = len(nums) - 1

		while best_reachable < length:
			while i <= best_reachable:
				new_best_reachable = max(new_best_reachable, i+nums[i])
				i += 1
			best_reachable = new_best_reachable
			new_best_reachable = 0
			count += 1

		return count


