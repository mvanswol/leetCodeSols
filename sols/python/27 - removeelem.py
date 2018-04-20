#
#
# Created By : Mitchell Van Swol
# Date : 3/19/2018
#

import sys

# remove all elements of a given value
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        start_idx = 0
        for elem in nums:
        	if elem != val:
        		nums[start_idx] = elem
        		start_idx = start_idx + 1

        return start_idx