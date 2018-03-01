#
#
# Created By : Mitchell Van Swol
# Date : 2/23/2018
#

import sys
# find if 3 numbers add up to a target

class Solution(object):
	def threeSumClosest(self, nums, target):

		if len(nums) < 3:
			return float("-inf")

		nums.sort()
		curr_best = nums[0] + nums[1] + nums[2]
		for i in range(0, len(nums) - 2):
			if i > 0 and nums[i] == nums[i-1]:
				continue

			start = i + 1
			end = len(nums) - 1
			while start < end:
				total = (nums[i] + nums[start] + nums[end])

				if total == target:
					return target
				
				if abs(total - target) < abs(curr_best - target):
					curr_best = total

				if total < target:
					start = start + 1
				elif total > target:
					end = end - 1


		return curr_best




input_file = open(sys.argv[1])
input_list = [int(x) for x in input_file.readline().strip("\n").split()]
input_target = int(input_file.readline().strip("\n"))
print(Solution().threeSum(input_list))