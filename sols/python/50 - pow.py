#
#
# Created By : Mitchell Van Swol
# Date : 6/14/2018
#

import sys

# calculate the power of a number
class Solution(object):
	def myPow(self, x, n):

		if x == 0 and n == 0:
			return float("-inf")

		if n < 0:
			x = 1.0 / x

		res = 1
		expo = abs(n)

		while expo > 0:

			if expo % 2:
				res = res * x
			x = x * x
			expo = expo / 2

		return res
