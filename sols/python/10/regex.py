#
#
# Created By : Mitchell Van Swol
# Date : 2/20/2018
#

# Implement a simple regex parser


# first approach : use recursion to check if regex is valid
# better approach is to use DP to store results of if the regex
# is valid up to a certain point in the string at the position of the
# regex

class Solution(object):
	def isMatch(self, s ,p):
		# create lookup table for dp solution
		match_table = [[False] * (len(s) + 1) for x in range((len(p) + 1))]

		# base case both empty
		match_table[0][0] = True

		for i in range(1, len(p)):
			match_table[i+1][0] = match_table[i-1][0] and (p[i] == '*')

		for i in range(len(p)):
			for j in range(len(s)):
				if p[i] == '*':
					match_table[i+1][j+1] = match_table[i-1][j+1] or match_table[i][j+1]

					if p[i-1] == s[j] or p[i-1] == '.':
						match_table[i+1][j+1] |= match_table[i+1][j]

				else:
					match_table[i+1][j+1] = match_table[i][j] and (p[i] == s[j]  or p[i] == '.')

		return match_table[-1][-1]

input_file = open(sys.argv[1])
input_string = input_file.readline().strip('\n')
input_regex = input_file.readline().strip('\n')
print(Solution().isMatch(input_string, input_regex))


