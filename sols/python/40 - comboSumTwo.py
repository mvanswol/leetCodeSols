#
#
# Created By : Mitchell Van Swol
# Date : 5/9/2018
#

import sys

# find all combos that add up to a target, using only each elem once
class Solution(object):
	def combinationSum2(self, candidates, target):

		if not candidates:
			return []

		result = []
		candidates.sort()
		self.recursiveComboSum(candidates, target, 0, [], result)
		return result

	def recursiveComboSum(self, candidates, target, idx, seq, result):

		if target < 0:
			return

		if target == 0 and seq not in result:
			result.append(seq)
			return

		for i in range(idx, len(candidates)):
			if i > 1 and candidates[i] == candidates[i-1]:
				continue
			self.recursiveComboSum(candidates[:i] + candidates[i+1:], target - candidates[i], i,
				                   seq + [candidates[i]], result)