#
#
# Created By : Mitchell Van Swol
# Date : 9/4/2018
#

# add one to a list of numbers
class Solution(object):
	def plusOne(self, digits):


		carry = 1
		result = []
		temp = 0
		for num in digits[::-1]:
			temp = num + carry
			if temp > 9:
				temp = 0
				carry = 1
			else:
				carry = 0
			result = [temp] + result

		if carry:
			result = [carry] + result

		return result