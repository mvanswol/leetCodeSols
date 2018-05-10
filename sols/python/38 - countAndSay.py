#
#
# Created By : Mitchell Van Swol
# Date : 5/9/2018
#

import sys

# Count and Say Game

class Solution(object):
	def countAndSay(self, n):

		if n == 1:
			return "1"

		string = self.countAndSay(n-1)
		result = ""
		count = 0

		for i in range(len(string)):
			if i > 0 and string[i] != string[i-1]:
				result += str(count) + s[i-1]
				count = 1
			else:
				count += 1

		result += str(count) + string[-1]
		return result 
