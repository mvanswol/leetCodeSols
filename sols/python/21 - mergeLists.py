#
#
# Created By : Mitchell Van Swol
# Date : 3/12/2018
#

import sys


# merge two sorted lists

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def mergeTwoLists(self, l1, l2):

		# go through each node and see which one is greater, 
		# then append to the list
		head = curr = ListNode(None)

		while l1 and l2:
			if l1.val < l2.val:
				curr.next = l1
				l1 = l1.next
			else:
				curr.next = l2
				l2 = l2.next

			curr = curr.next

		curr.next = l1 or l2
			
		return head.next
