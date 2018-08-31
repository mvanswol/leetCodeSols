#
#
# Created By : Mitchell Van Swol
# Date : 8/30/2018
#

# Given a list of elements containing the numbers 1 to n, where n <= 9
# return the kth permutation of the sequence

import math

class Solution(object):
	def getPermutation(self, n, k):

		if n <= 0 or n >= 10:
			return ''

		if k <= 0:
			return None

		val_list = [str(i) for i in range (1,n+1)]
		fact = 1
		for i in range(1, n+1):
			fact *= i

		k = k - 1
		res = ''
		while n > 0:
			fact = fact / n
			n = n - 1
			idx, k = divmod(k, fact)
			res += val_list.pop(idx)

		return res





