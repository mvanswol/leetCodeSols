#
#
# Created By : Mitchell Van Swol
# Date : 2/7/2018
#

import sys

# check if a number is a palindrome
# solution is O(n) where n is the number of digits
# this is also O(log(a)) where a is the integer

#string process is slightly faster
class SolutionStr(object):
	def isPalindrome(self, x):
		return int(str(abs(x))[::-1]) == x


class Solution(object):
	def isPalindrome(self, x):

		if x < 0:
			return False

		pow_ten = 1
		while x / pow_ten >= 10:
			pow_ten *= 10

		while x:
			left_digit = x / pow_ten
			right_digit = x % 10

			if left_digit != right_digit:
				return False

			x = (x % pow_ten) / 10
			pow_ten //= 100

		return True

input_file = open(sys.argv[1])
input_int = int(input_file.readline().strip("\n"))
print(SolutionStr().isPalindrome(input_int))



