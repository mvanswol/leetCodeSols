#
#
# Created By : Mitchell Van Swol
# Date : 9/4/2018
#

# add binary numbers
class Solution(object):
	def addBinary(self, a, b):

		len_a = len(a)
		len_b = len(b)
		diff = abs(len_a - len_b)
		carry = 0
		result = ""
		if len_a > len_b:
			b = "0"*diff + b
		elif len_a < len_b:
			a = "0"*diff + a

		print(a)
		print(b)

		for i in range(max(len_a, len_b))[::-1]:
			temp = int(a[i]) + int(b[i]) + carry
			if temp >= 2:
				carry = 1
				temp = temp % 2
			else:
				carry = 0

			result = str(temp) + result

		if carry:
			result = str(carry) + result

		return result



