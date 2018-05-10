#
#
# Created By : Mitchell Van Swol
# Date : 5/9/2018
#

import sys

# Solve Sudoku

class Solution(object):
	def solveSudoku(self, board):
		self.board = board
		self.validNumbers = ["1","2","3",
		                     "4","5","6",
		                     "7","8","9"]
		self.recursiveSolve()

	def findOpen(self):
		for i in range(9):
			for j in range(9):
				if self.board[i][j] == '.':
					return i,j

		return -1,-1

	def isValid(self, row, col, char):
		box_row = row - row % 3
		box_col = col - col % 3

		if self.check_row_col(row, col, char) and self.check_box(box_row, bow_col, char):
			return True
		return False

	def check_row_col(self, row, col, char):

		for i in range(9):
			if self.board[row][i] == char or \
			   self.board[i][col] == char:
			   return False
		return True

	def check_box(self, row, col, char):

		for i in range(row, row+3):
			for j in range(col, col+3):
				if self.board[i][j] == char:
					return False

		return True

	def recursiveSolve(self):

		row, col = self.findOpen()

		if row == -1 and col == -1:
			return True

		for num in self.validNumbers:
			if self.isValid(row, col, num):
				self.board[row][col] = num
				if self.recursiveSolve():
					return True

				self.board[row][col] = "."
		return False








