#
#
# Created By : Mitchell Van Swol
# Date : 8/30/2018
#

# find min path

class Solution(object):
	def minPathSum(self, grid):
		row = len(grid)
		col = len(grid[0])
		costs = [[0]*col for _ in range(row)]

		costs[0][0] = grid[0][0]
		for i in range(1,row):
			costs[i][0] = grid[i][0] + costs[i-1][0]

		for j in range(1,col):
			costs[0][j] = grid[0][j] + costs[0][j-1]


		for i in range(1,row):
			for j in range(1,col):
				costs[i][j] = grid[i][j] + min(costs[i-1][j], costs[i][j-1])


		return costs[-1][-1]
