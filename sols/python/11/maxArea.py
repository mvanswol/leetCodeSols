#
#
# Created By : Mitchell Van Swol
# Date : 2/21/2018
#

import sys
# max area in a container of water
# just scan the array looking for the max area

class Solution(object):
	def maxArea(self, height):

		if not height or len(height) < 2:
			return 0

		left = 0
		right = len(height) - 1
		max_area = 0
		tmp_area = 0

		while left < right:

			tmp_area = min(height[left], height[right]) * (right - left)

			if tmp_area > max_area:
				max_area = tmp_area

			if height[left] < height[right]:
				left = left + 1
			else:
				right = right - 1

		return max_area

input_file = open(sys.argv[1])
in_list = [int(x) for x in input_file.readline().split()]
print(Solution().maxArea(in_list))
