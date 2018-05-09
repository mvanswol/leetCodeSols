#
#
# Created By : Mitchell Van Swol
# Date : 5/8/2018
#

import sys

# find the longest valid parenthesis

class Solution(object):
	def longestValidParentheses(self, s):

		stack = [0]
		longest_valid = 0

		for char in s:
			if char == "(":
				stack.append(0)
			else:
				if len(stack) > 1:
					value = stack.pop()
					stack[-1] += value + 2
					longest_valid = longest_valid if longest_valid > \
					                stack[-1] else stack[-1]
				else:
					stack = [0]

		return longest_valid

