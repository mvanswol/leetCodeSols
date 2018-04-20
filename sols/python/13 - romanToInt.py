#
#
# Created By : Mitchell Van Swol
# Date : 2/21/2018
#

import sys
# convert roman numeral into int

class Solution(object):
	def romanToInt(self, s):

		if not s:
			return -1

		rom_dict = {'I' : 1, 'V' : 5, 'X' : 10,
		            'L' : 50, 'C' : 100, 'D' : 500,
		            'M' : 1000}

		output = 0
		for i in range(0, len(s) - 1):
			if rom_dict[s[i]] < rom_dict[s[i+1]]:
				output = output - rom_dict[s[i]]
			else:
				output = output + rom_dict[s[i]]

		return output + rom_dict[s[len(s)-1]]


input_file = open(sys.argv[1])
in_string = input_file.readline().strip("\n")
print(Solution().romanToInt(in_string))