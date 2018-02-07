#
#
# Created By : Mitchell Van Swol
# Date : 2/6/2018
#

# Find the longest palindromic substring

import sys

# Brute force algorithm : 
# create all substrings
# check if a given substring is a palindrome
# if true check if length is greater than the longest seen so far

#Better idea, Dynamic Programming
#Create a table of substrings and check and see if 
# if a substring of the current substring is a palindrome
class Solution(object):
	def longestPalindrome(self, s):
		size_s = len(s)

		if not size_s or size_s == 1:
			return s

		max_len = 1
		substring_table = [[0 for i in range(size_s)] 
							for j in range(size_s)]

		for i in range(size_s):
			substring_table[i][i] = 1

		start_idx = 0
		for i in range(size_s - 1):
			if s[i] == s[i+1]:
				substring_table[i][i+1] = 1
				start_idx = i
				max_len = 2

		for j in range(3, size_s+1):
			for i in range(size_s - j + 1):
				k = i + j - 1
				if substring_table[i+1][k-1] and \
				   s[i] == s[k]:
				   	substring_table[i][k] = 1

				   	if j > max_len:
				   		start_idx = i
				   		max_len = j

		print(start_idx)
		print(max_len)

		return s[start_idx:start_idx + max_len]

input_file = open(sys.argv[1])
input_line = input_file.readline()
string = input_line.strip("\n")
print(string)
print(Solution().longestPalindrome(string))