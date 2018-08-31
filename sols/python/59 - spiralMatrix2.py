#
#
# Created By : Mitchell Van Swol
# Date : 8/16/2018
#

class Solution(object):
	def generateMatrix(self, n):

		if n == 0:
			return []

		output, low = [], n*n+1
		while low > 1:
			low, high = low - len(output), low
			output = [range(low, high)] + zip(*output[::-1])


		return output


print(Solution().generateMatrix(3))

