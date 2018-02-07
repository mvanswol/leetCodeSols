#
#
# Created By : Mitchell Van Swol
# Date : 2/6/2018
#

import sys

# convert the given string to a zigzag pattern

# basic idea is that we map out the string in a zig zag
# pattern and then join the strings together
# O(n) solution

class Solution(object):
	def convert(self, s, numRows):

		if numRows == 1 or numRows >= len(s):
			return s

		idx, step = 0, 1
		end = numRows - 1
		ans = [""] * numRows

		for char in s:
			ans[idx] += char
			if not idx:
				step = 1
			elif idx == end:
				step = -1

			idx += step

		return "".join(ans)


input_file = open(sys.argv[1])
input_line = input_file.readline()
string = input_line.strip("\n")
num_rows = int(input_file.readline().strip("\n"))
print(string)
print(Solution().convert(string, num_rows))




