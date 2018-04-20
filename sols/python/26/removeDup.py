#
#
# Created By : Mitchell Van Swol
# Date : 3/19/2018
#

import sys

# remove duplicates from array

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        start_idx = 0
        last_val = -sys.maxsize - 1
        
        for elem in nums:
            if last_val != elem:
                last_val = elem
                nums[start_idx] = last_val
                start_idx = start_idx + 1
                
        return start_idx