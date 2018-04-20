#
#
# Created By : Mitchell Van Swol
# Date : 3/19/2018
#

import sys

# implement division without using multiplication
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sol = 0
        positive = (dividend > 0) is (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)

        while dividend >= divisor:
        	temp = divisor
        	i = 1 
        	while dividend >= temp:
        		dividend = dividend - temp
        		sol = sol + i
        		i = i << 1
        		temp = temp << 1

        if not positive:
        	sol = -sol

        return min(max(-2147483648, sol), 2147483647)


