#
#
# Created By : Mitchell Van Swol
# Date : 5/9/2018
#

import sys

# find all combos that add up to a target
class Solution(object):
	def combinationSum(self, candidates, target):

		if not candidates:
			return []

		result = []
		candidates.sort()
		self.recursiveComboSum(candidates, target, 0, [], result)
		return result

	def recursiveComboSum(self, candidates, target, idx, seq, result):

		if target < 0:
			return

		if target == 0:
			result.append(seq)
			return

		for i in range(idx, len(candidates)):
			self.recursiveComboSum(candidates, target - candidates[i], i,
				                   seq + [candidates[i]], result)