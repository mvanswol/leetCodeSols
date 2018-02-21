#
#
# Created By : Mitchell Van Swol
# Date : 2/7/2018
#

import sys

# write an atoi program

# Just do all of the check and make sure that its a number
# algorithm is O(n) where n is the length of the string

class Solution(object):
	def myAtoi(self, s):
		split_input = s.split()

		if not split_input:
			#print("Input is empty or only has whitespace")
			return 0

		# peek at first char for sign
		skip = 1 if split_input[0][0] in ['-', '+'] else 0
		signed = 1 if split_input[0][0] == '-' else 0

		int_val = 0
		for char in split_input[0][skip:]:
			if ord(char) >= 48 and  ord(char) <= 57:
				int_val = int_val * 10 + (ord(char) - 48)
			else:
				break

		if int_val > 2147483648 and signed:
			#print("Underflow integer is too small")
			return -2147483648
		elif int_val > 2147483647 and not signed:
			#print("Overflow integer is too large")
			return 2147483647

		return int_val if not signed else int_val * -1



input_file = open(sys.argv[1])
input_string = input_file.readline().strip("\n")
output = Solution().myAtoi(input_string)
print("input : {}\noutput type: {}\noutput : {}".format(
	  input_string,
	  type(output),
	  output))