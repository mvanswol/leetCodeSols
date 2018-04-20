#
#
# Created By : Mitchell Van Swol
# Date : 2/6/2018
#

import sys

# reverse the digits of an usigned integer
# convert int to string
# reverse string, bounds check


class Solution(object):
	def reverse(self, x):

		rev_num = 0
		base_pos = 1

		signed = True if x < 0 else False

		if signed:
			x = x * -1

		while x:
			pos_num = x % 10
			rev_num = rev_num * 10 + pos_num
			x = x / 10

		if signed:
			if rev_num > 2147483648:
				return 0
			else:
				return rev_num * -1
		elif rev_num > 2147483647:
			return 0
		else:
			return rev_num




input_file = open(sys.argv[1])
input_int = int(input_file.readline().strip("\n"))
print(Solution().reverse(input_int))