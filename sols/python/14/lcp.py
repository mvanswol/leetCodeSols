#
#
# Created By : Mitchell Van Swol
# Date : 2/23/2018
#

import sys
# find the longest common prefix between some strings

#algo : find the shortest string, which is O(n * len(longest_n))
# then loop through each character of the shortest and see if
# each character at each position matches otherwise, return what's
# matched so far

class Solution(object):
	def longestCommonPrefix(self, strs):

		if not strs:
			return ""

		shortest_str = min(strs, key=len)

		for idx, char in enumerate(shortest_str):
			for curr_str in strs:
				if curr_str[idx] != char:
					return curr_str[:idx]

		return shortest_str

input_file = open(sys.argv[1])
in_list = [x.strip("\n") for x in input_file.readlines()]
print(Solution().longestCommonPrefix(in_list))