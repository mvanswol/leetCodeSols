#
#
# Created By : Mitchell Van Swol
# Date : 2/28/2018
#

import sys

# given a list of elements see if 4 elements add up to a
# given sum

# solution : O(n^2 * log(n))

class Solution(object):
	def binSearh(self, nums, target, low, high):

		if low > high:
			return []

		mid = low + (high - low) / 2
		if nums[mid][0] == target:
			output_list = [nums[mid]]

			low_idx = mid - 1
			high_idx = mid + 1
			while low_idx > 0 and nums[low_idx][0] == target:
				output_list.append(nums[low_idx])
				low_idx = low_idx - 1

			while high_idx < len(nums) and nums[high_idx][0] == target:
				output_list.append(nums[high_idx])
				high_idx = high_idx + 1

			return output_list

		if nums[mid][0] > target:
			return self.binSearh(nums, target, low, mid - 1)
		else:
			return self.binSearh(nums, target, mid + 1, high)


	def fourSum(self, nums, target):

		output_list = []
		if not nums or len(nums) < 4:
			return output_list


		sum_two_list = []
		for i in range(0, len(nums) - 1):
			for j in range(i+1, len(nums)):
				sum_two_list.append([nums[i] + nums[j], i, j])

		sum_two_list.sort(key=lambda tup: tup[0])

		for tup in sum_two_list:
			new_target = target - tup[0]

			candidate_list = self.binSearh(sum_two_list, new_target, 0, len(sum_two_list) - 1)
			for candidate in candidate_list:
				if tup[1] != candidate[1] and tup[1] != candidate[2] \
				   and tup[2] != candidate[1] and tup[2] != candidate[2]:
					
					val_list = sorted([nums[tup[1]], nums[tup[2]], nums[candidate[1]],
						              nums[candidate[2]]])

					if val_list not in output_list:
						output_list.append(val_list)

		return output_list 


	    






input_file = open(sys.argv[1])
input_list = [int(x) for x in input_file.readline().strip("\n").split()]
input_target = int(input_file.readline().strip("\n"))
print(Solution().fourSum(input_list, input_target))