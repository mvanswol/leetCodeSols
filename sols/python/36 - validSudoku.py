#
#
# Created By : Mitchell Van Swol
# Date : 5/9/2018
#

import sys

# Check if sudoku board is valid

class Solution(object):
	def isValidSudoku(self, board):

		valid_row = [{}, {}, {},
		             {}, {}, {},
		             {}, {}, {}]
		valid_col = [{}, {}, {},
		             {}, {}, {},
		             {}, {}, {}]
		valid_box = [{}, {}, {},
		             {}, {}, {},
		             {}, {}, {}]


		for i in range(len(board)):
			for j in range(len(board[0])):
				char = board[i][j]
				offset = 3 * int(i/3) + int(j/3)

				if char == '.':
					continue

				# check to see if we've already seen a valid number
				elif char not in valid_row[i] and char not in valid_col[j] and \
				     char not in valid_box[offset]:

				     valid_row[i][char] = 1
				     valid_col[j][char] = 1
				     valid_box[offset][char] = 1
				else:
					return False

		return True