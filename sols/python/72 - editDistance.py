#
#
# Created By : Mitchell Van Swol
# Date : 11/21/2018
#

# Given two string compute the edit distance between the two string

import sys

class Solution(object):
	def minDistance(self, word1, word2):

		if not word1:
			return len(word2)

		if not word2:
			return len(word1)


		dp_mat = [[0 for _ in range(len(word2) + 1)] 
		           for x in range(len(word1)+1)]

		for i in range(len(word1)+1):
			dp_mat[i][0] = i

		for j in range(len(word2)+1):
			dp_mat[0][j] = j


		for i in range(1, len(word1) + 1):
			for j in range(1, len(word2) + 1):
				if word1[i-1] == word2[j-1]:
					dp_mat[i][j] = dp_mat[i-1][j-1]

				else:
					dp_mat[i][j] = min(dp_mat[i-1][j] + 1, 
						                   dp_mat[i-1][j-1] + 1,
						                   dp_mat[i][j-1] + 1)


		return dp_mat[-1][-1]