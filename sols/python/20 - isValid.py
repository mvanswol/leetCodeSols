#
#
# Created By : Mitchell Van Swol
# Date : 2/28/2018
#

import sys


# check if a string containing parens are valid

class Solution(object):
	def isValid(self, s):

		if len(s) == 0:
			return True 

		stack = []
		for char in s:
			if char == '(' or char == '[' \
				or char == '{':
				stack.insert(0, char)

			elif len(stack) == 0:
				return False
			elif (char == ')' and stack[0] == '(') or \
				(char == ']' and stack[0] == '[') or \
				(char == '}' and stack[0] == '{'):
				stack.pop(0)
			else:
				return False


		if len(stack) == 0:
			return True
		else:
			return False


input_file = open(sys.argv[1])
input_string = input_file.readline().strip("\n")
print(Solution().isValid(input_string))
