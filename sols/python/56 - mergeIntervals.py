#
#
# Created By : Mitchell Van Swol
# Date : 6/24/2018
#

import sys

# Merge Intervals problem

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):
	def merge(self, intervals):

		if not intervals:
			return []

		output = []
		intervals.sort(key= lambda x: x.start)
		curr_start = intervals[0].start
		curr_end = intervals[0].end


		for interval in intervals:

			# begin a new interval
			if interval.start > curr_end:
				output.append([curr_start, curr_end])
				curr_start = interval.start
				curr_end = interval.end
			else:
				if interval.end > curr_end:
					curr_end = interval.end

		output.append([curr_start, curr_end])
		return output





