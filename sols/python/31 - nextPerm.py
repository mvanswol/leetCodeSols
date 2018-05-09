#
#
# Created By : Mitchell Van Swol
# Date : 5/8/2018
#

import sys

# find the next iteration in a permutation in place


# following the wikipedia article for the next lexicographic order 
# permutation

# find k such that a[k] < a[k+1], and k is the largest
# find largest j > k, such that a[k] < a[j]

class Solution(object):
	def nextPermutation(self, nums):

		if not nums:
			return nums

		len_nums = len(nums)
		k, j = len_nums - 2, len_nums - 1

		while k >= 0 and nums[k] >= nums[k+1]: 
			k = k -1
		while j > k and nums[j] <= nums[k]:
			j = j - 1

		nums[k], nums[j] = nums[j], nums[k]
		nums[k+1:] = nums[k+1][:-1]







