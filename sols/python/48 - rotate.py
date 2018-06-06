#
#
# Created By : Mitchell Van Swol
# Date : 6/5/2018
#

import sys

# reverse a 2d List
class Solution(object):
	def rotate(self, matrix):
		length = len(matrix)

		for i in range(length):
			for j in range(i+1, length):
				matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

		for i in range(length):
			for j in range(length/2):
				matrix[i][j], matrix[i][length - j - 1] = matrix[i][length - j - 1], matrix[i][j]