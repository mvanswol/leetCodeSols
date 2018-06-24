#
#
# Created By : Mitchell Van Swol
# Date : 6/18/2018
#

import sys

# return an m by n matrix in spiral order
class Solution(object):
	def spiralOrder(self, matrix):

		result = []

		# loop through the entire matrix
		while matrix:
			# remove the first row and add it to the result
			result = result + matrix.pop(0)

			# add the last element of all remain rows
			if matrix and matrix[0]:
				for row in matrix:
					result.append(row.pop())

			# Add the last row in reverse
			if matrix:
				result = result + matrix.pop()[::-1]

			# Add the first element of each remaining row in reverse order
			if matrix and matrix[0]:
				for row in matrix[::-1]:
					result.append(row.pop(0))

		return result



