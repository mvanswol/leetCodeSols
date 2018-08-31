#
#
# Created By : Mitchell Van Swol
# Date : 8/30/2018
#

# find the number of unique paths

class Solution(object):
	def __init__(self):
		self.m = 0
		self.n = 0
		self.pathsArr = None

	def uniquePaths(self, m, n):
		if not m or not n:
			return 0

		self.m = m
		self.n = n
		self.pathsArr = [[0]*n for _ in range(self.m)]
		for i in range(self.n):
			self.pathsArr[0][i] = 1
		for i in range(self.m):
			self.pathsArr[i][0] = 1

		for i in range(1, self.m):
			for j in range(1, self.n):
				self.pathsArr[i][j] = self.pathsArr[i-1][j] + self.pathsArr[i][j-1]

		return self.pathsArr[self.m - 1][self.n - 1]
		

