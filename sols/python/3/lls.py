#
#
# Created By : Mitchell Van Swol
# Date : 1/23/2018
#

# Given a string, find the length of the longest substring without repeating characters

import sys

# brute force is find all substrings
# find the longest without repeating characters
# this is O(n^2) where n is the lenght of the string

# Better solution: use extra space and scan the list only once
# we will use a extra lookup table to keep track of whether or not
# we've seen the specified character before
# if so then reset our counter
def lengthOfLongestSubstring(s):

	if len(s) == 0:
		return 0

	num_map = {}
	for i in range(0,255):
		num_map[i] = -1

	cur_len = 1
	max_len = 1

	num_map[ord(s[0])] = 0

	for index in range(1, len(s)):
		off_index = ord(s[index])
		prev_index = num_map[off_index]

		if prev_index == -1 or (index - cur_len > prev_index):
			cur_len += 1
		else:
			if cur_len > max_len:
				max_len = cur_len

			cur_len = index - prev_index

		num_map[off_index] = index

	return max_len if max_len > cur_len else cur_len
	

input_file = open(sys.argv[1])
in_string = input_file.readline()
print(in_string)
print(lengthOfLongestSubstring(in_string))