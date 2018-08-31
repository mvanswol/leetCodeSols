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

	def uniquePathsWithObstacles(self, obstacleGrid):
		if not obstacleGrid:
			return None

		self.m = len(obstacleGrid)
		self.n = len(obstacleGrid[0])
		self.pathsArr = [[0]*self.n for _ in range(self.m)]

		for i in range(self.m)[::-1]:
			for j in range(self.n)[::-1]:
				if not obstacleGrid[i][j]:
					if i == self.m-1 and j == self.n-1:
						self.pathsArr[i][j] = 1
					if i+1 < self.m:
						self.pathsArr[i][j] += self.pathsArr[i+1][j]
					if j+1 < self.n:
						self.pathsArr[i][j] += self.pathsArr[i][j+1]

		return self.pathsArr[0][0]
		

