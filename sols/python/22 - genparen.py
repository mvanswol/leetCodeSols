#
#
# Created By : Mitchell Van Swol
# Date : 3/12/2018
#

import sys

# generate all pairs of n parenthesis
class Solution(object):
	# solution is the dynamically geneate lower pairs of parenthesis and construct a progressively bigger pair
	# other eaiser solution is to use recursion
	def generateParenthesis(self, n):
		def generateHelper(paren_str, left, right, output_list=[]):
			if left:
				generateHelper(paren_str + '(', left - 1, right, output_list)
			if right > left:
				generateHelper(paren_str + ')', left, right - 1, output_list)

			if not right:
				output_list.append(paren_str)

			return output_list

		return generateHelper('', n, n)