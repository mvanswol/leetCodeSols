#
#
# Created By : Mitchell Van Swol
# Date : 1/23/2018
#

# Find the median of two sorted arrays

# Brute force algorithm :
# Sequential merge the two arrays and then find the median
# this is O(m + n) since you would have to go through each element of the array

# This challenge requires a runtime of O(log(m + n))
# so we need to do better than that

# Approach : Binary Search the arrays 

import sys
import math
class Solution(object):
	def findKthOne(self, nums, k):
		return nums[k]

	def findKthTwo(self, nums1, nums2, k):
		if len(nums1) == 0:
			return self.findKthOne(nums2, k)
		elif len(nums2) == 0:
			return self.findKthOne(nums1, k)
		mid_nums1 = len(nums1) / 2
		mid_nums2 = len(nums2) / 2

		if (mid_nums1 + mid_nums2) < k:
			if nums1[mid_nums1] > nums2[mid_nums2]:
				return self.findKthTwo(nums1, nums2[mid_nums2+1:], k - mid_nums2-1)
			else:
				return self.findKthTwo(nums1[mid_nums1+1:], nums2, k - mid_nums1-1)
		else:
			if nums1[mid_nums1] > nums2[mid_nums2]:
				return self.findKthTwo(nums1[:mid_nums1], nums2, k)
			else:
				return self.findKthTwo(nums1, nums2[:mid_nums2], k)

	def findMedianSortedArrays(self, nums1, nums2):
		size_nums1 = len(nums1)
		size_nums2 = len(nums2)
		total_size = size_nums1 + size_nums2

		if not total_size:
			return float("-inf")

		if total_size & 1:
			return float(self.findKthTwo(nums1, nums2, total_size/2))
		else:
			return float(self.findKthTwo(nums1, nums2, total_size/2 - 1) +
				         self.findKthTwo(nums1, nums2, (total_size/2))) * 0.5


input_file = open(sys.argv[1])
list_one = sorted([int(x) for x in input_file.readline().split()])
list_two = sorted([int(x) for x in input_file.readline().split()])
print(list_one)
print(list_two)
print(Solution().findMedianSortedArrays(list_one, list_two))





