#
#
# Created By : Mitchell Van Swol
# Date : 6/5/2018
#

import sys

# return all possible permutations
# use DFS algorithm, except only unique
# perms
class Solution(object):
	def permuteUnique(self, nums):
		"""
		return all possible permutations
		"""
		nums.sort()
		perm_list = []
		self.dfs(nums, [], perm_list)
		return perm_list

	def dfs(self, nums, temp_list, perm_list):

		if not nums:
				perm_list.append(temp_list)

		for i, val in enumerate(nums):
			if i > 0 and nums[i] == nums[i - 1]:
				continue
			self.dfs(nums[:i]+nums[i+1:], temp_list+[val],perm_list)