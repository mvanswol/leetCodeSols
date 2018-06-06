#
#
# Created By : Mitchell Van Swol
# Date : 6/4/2018
#

import sys

# multiply two strings
class Solution(object):
	def multiply(self, num1, num2):
		
		if not num1 or not num2:
			return 
		a = 0
		for i, num in enumerate(num1[::-1]):
			a += (ord(num) - 48) * 10 ** i

		b = 0
		for i, num in enumerate(num2[::-1]):
			b += (ord(num) - 48) * 10 ** i

		return str(a * b)

		