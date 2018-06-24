#
#
# Created By : Mitchell Van Swol
# Date : 6/24/2018
#

class Solution(object):
	def lengthOfLastWord(self,s):
		split_list = s.split()
		return len(split_list[-1]) if len(split_list) else 0