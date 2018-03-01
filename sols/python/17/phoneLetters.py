#
#
# Created By : Mitchell Van Swol
# Date : 2/26/2018
#

import sys

# Given phone digits convert them to letters

class Solution(object):
    def letterCombinations(self, digits):

    	digits_map = {'1' : "",
    	              '2' : "abc",
    	              '3' : "def",
    	              '4' : "ghi",
    	              '5' : "jkl",
    	              '6' : "mno",
    	              '7' : "pqrs",
    	              '8' : "tuv",
    	              '9' : "wxyz",
    	              '0' : ""}
    	output = [''] if digits else []

    	for digit in digits:
    		curr_combos = []
    		for char in digits_map[digit]:
    			for combo in output:
    				curr_combos.append(combo + char)
    		output = curr_combos

    	return output





input_file = open(sys.argv[1])
input_string = input_file.readline().strip("\n")
print(Solution().letterCombinations(input_string))