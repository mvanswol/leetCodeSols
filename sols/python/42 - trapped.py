#
#
# Created By : Mitchell Van Swol
# Date : 5/25/2018
#

import sys

# find the amount of water that can be trapped
class Solution(object):
	def trap(self, height):

		total = 0
		if len(height) <= 1:
			return total

		length = len(height)
		left_max = height[0]
		left_max_list = [left_max]
		right_max = height[-1]
		right_max_list = [right_max]

		for i in range(1, length):
			if height[i] > left_max:
				left_max = height[i]
			if height[length - 1 - i] > right_max:
				right_max = height[length - 1 - i]

			left_max_list.append(left_max)
			right_max_list.append(right_max)

		for i in range(length):
			min_max = min(left_max_list[i], right_max_list[length -1 - i])
			total += (min_max - height[i])

		return total



