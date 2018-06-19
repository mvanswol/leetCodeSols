#
#
# Created By : Mitchell Van Swol
# Date : 6/14/2018
#

import sys

# return list of all groups of anagrams
class Solution(object):
	def groupAnagrams(self, strs):

		# create a dictionary of anagrams
		anagrams = {}

		for string in strs:

			sorted_string = ''.join(sorted(string))
			if sorted_string in anagrams:
				anagrams[sorted_string].append(string)
			else:
				anagrams[sorted_string] = [string]


		return [anagrams[key] for key in anagrams]

