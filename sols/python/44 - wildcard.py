#
#
# Created By : Mitchell Van Swol
# Date : 6/4/2018
#

import sys

# regex wild card matching
class Solution(object):
	def isMatch(self, s, p):

		dp_matrix = [[False] * (len(s) + 1) for _ in range(len(p)+1)]

		dp_matrix[0][0] = True # empty case is true

		for i in range(len(p)):
			if p[i] == '*':
				dp_matrix[i+1][0] = True
			else:
				break

		for i in range(1, len(p)+1):
			for j in range(1, len(s)+1):
				if p[i-1] == '*':
					dp_matrix[i][j] = dp_matrix[i][j - 1] or dp_matrix[i-1][j]
				else:
					if p[i-1] == '?' or p[i-1] == s[j-1]:
						dp_matrix[i][j] = dp_matrix[i-1][j-1]
		
		return dp_matrix[len(p)][len(s)]   



