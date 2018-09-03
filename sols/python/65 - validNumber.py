#
#
# Created By : Mitchell Van Swol
# Date : 9/3/2018
#

# check if number is valid

class Solution(object):
	def isNumber(self, s):

		# remove leading whitespace
		stripped_s = s.strip()

		def isUnsign(s):
			return s != "" and filter(lambda c: '0' <= c <= '9', s) == s

		def isSigned(s):
			return s != "" and s[0] in ['-', '+'] and isUnsign(s[1:]) or isUnsign(s)
		
		
		def isInteger(s):
			return isSigned(s) 
		
		def isFloat(s):
			float_point = s.find('.')
			if float_point != -1:
				if isInteger(s[:float_point]):
					return s[float_point + 1:] == "" or isUnsign(s[float_point + 1:])
				elif s[:float_point] == "" or s[:float_point] == "+" or s[:float_point] == "-":
					return isUnsign(s[float_point + 1:])
				else:
					return False
			else:
				return isInteger(s)
		
		def isExpo(s):
			e = s.find('e')
			if e != -1:
				return isFloat(s[:e]) and isInteger(s[e + 1:])
			else:
				return isFloat(s)
			
		return isExpo(stripped_s)
