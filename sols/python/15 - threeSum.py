#
#
# Created By : Mitchell Van Swol
# Date : 2/23/2018
#

import sys
# find if 3 numbers add up to 0

class Solution(object):
	def threeSum(self, nums):
		output_list = []

		if len(nums) < 3:
			return output_list

		nums.sort()
		for i in range(0, len(nums) - 2):
			if i > 0 and nums[i] == nums[i-1]:
				continue

			start = i + 1
			end = len(nums) - 1
			while start < end:
				total = (nums[i] + nums[start] + nums[end])
				if total < 0:
					start = start + 1
				elif total > 0:
					end = end - 1
				else:
					output_list.append([nums[i], nums[start], nums[end]])
					while start < end and nums[start] == nums[start + 1]:
						start = start + 1
					while start < end and nums[end] == nums[end - 1]:
						end = end - 1

					start = start + 1
					end = end - 1


		return output_list




input_file = open(sys.argv[1])
input_list = [int(x) for x in input_file.readline().strip("\n").split()]
print(Solution().threeSum(input_list))