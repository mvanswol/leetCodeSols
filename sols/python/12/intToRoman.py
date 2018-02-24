#
#
# Created By : Mitchell Van Swol
# Date : 2/21/2018
#

import sys
# convert int to a roman numeral

class Solution(object):
	def intToRoman(self, num):

		if num < 1 or num > 3999:
			return ""

		rom_nums = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
		nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
		output = ""

		for i,j in enumerate(nums):
			while num >= j:
				output = output + rom_nums[i]
				num = num - j

			if num == 0:
				return output





input_file = open(sys.argv[1])
num = int(input_file.readline().strip("\n"))
print(Solution().intToRoman(num))