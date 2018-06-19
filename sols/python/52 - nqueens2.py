#
#
# Created By : Mitchell Van Swol
# Date : 6/18/2018
#

import sys

# solve the number of solutions to theN-queens problem
class Solution(object):
	def __init__(self):
		self.sol = []

	def totalNQueens(self, n):
		self.n = n
		self.board = [ ['.' for _ in range(self.n)] for _ in range(self.n)]
		self.solve(0)

		return len(self.sol)

	def solve(self, row):

		for i in range(self.n):
			if self.check_space(row,i):
				self.board[row][i] = 'Q'
				if row == self.n - 1:
					self.sol.append([''.join(row_string) for row_string in self.board])

				self.solve(row+1)
				self.board[row][i] = '.'


	def check_space(self, i, j):
		""" check to see if current placement is valid """

		# check Columns
		for k in range(i):
			if self.board[k][j] == 'Q':
				return False


		# check the diagonals
		x,y = i-1, j-1
		while x >= 0  and y >= 0:
			if self.board[x][y] == 'Q':
				return False
			x,y = x-1, y-1
			
		x,y = i-1, j+1
		while x >= 0 and y < self.n:
			if self.board[x][y] == 'Q':
				return False
			x,y = x-1, y+1


		return True